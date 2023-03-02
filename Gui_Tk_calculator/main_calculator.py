from tkinter import *

exercise = ""
number = ""
root = None
resultOutput = None

def resetCalculator():
    global exercise, number
    setEntryText(resultOutput, "0")
    exercise = ""
    number = ""

def calculate():
    global exercise, number
    expression = exercise +number
    if not expression:
        return
    try:
        result = eval(expression)
        setEntryText(resultOutput, result)
        exercise = ""
        number = str(result)
    except:
        resultOutput.configure(state='normal', bg='red')

def buildNumber(value: str):
    global exercise, number
    if value == "." and "." in number:
        return
    number += value
    result = exercise + number
    setEntryText(resultOutput, result)

def addOperation(value: str):
    global exercise, number
    if not number:
        if not exercise:
            return
        if exercise and exercise[-1] in operations:
            return
    exercise += number + value
    number = ""
    setEntryText(resultOutput, exercise)

def backspaceClicked(entry):
    global number, exercise
    if (not number) and (not exercise): 
        return
    elif number and not exercise:
        number = number[:-1]
    elif not number and exercise:
        exercise = exercise[:-1]
    elif number and exercise:
        number = number[:-1]
    deletLastCharFromEntry(resultOutput)
              
def setEntryText(entry, text):
    entry.config(state="normal")
    entry.delete(0, END)
    if text == '':
        text ='0'
    entry.insert(0, text)
    entry.config(state="readonly")
    
def buttonClicked(value: str):
    if value == "=":
        calculate()
    elif value == "AC":
        resetCalculator()
    elif value in digits or value == ".":
        buildNumber(value)
    elif value in operations:  #and number #and (exercise[-1] not in operations)
        addOperation(value)
    elif value == "←":
        backspaceClicked(resultOutput)
       
def deletLastCharFromEntry(entry):
    current_expression = entry.get()
    setEntryText(entry, current_expression[:-1])
        
def makeButton(parent, value: str):
    return Button(parent, text=value, font ='arial 18 bold', command=lambda m=value: buttonClicked(value))

root = Tk()
root.geometry("450x400+300+100")
root.title("CALCULATOR")
resultOutput = Entry(root, justify = RIGHT, font ='arial 20 bold', state = "disabled" )
setEntryText(resultOutput, "0")
resultOutput.insert(0, '0')
resultOutput.grid(column = 0, row = 0, columnspan = 4, sticky = "nswe", padx = 3, pady = 3)

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
operations = ["+", "-", "*", "/"]
buttonValues = [
    [7, 8, 9, "+"],
    [4, 5, 6, "-"],
    [1, 2, 3, "*"],
    [0, ".","AC", "/"],
    ["←", "="]
]

for rowIndex, row in enumerate(buttonValues):
    for columnIndex, value in enumerate(row):
        button = makeButton(root, str(value))
        if value == "=":
            button.grid(column = 3, row = rowIndex + 1, sticky = "nswe",padx = 1, pady = 1, ipadx = 5, ipady = 3)
        else:
            button.grid(column = columnIndex, row = rowIndex + 1, sticky = "nswe",padx = 1, pady = 1, ipadx = 5, ipady = 3)

        root.columnconfigure(index = columnIndex , weight= 1)
    root.rowconfigure(index = rowIndex + 1, weight= 1 )
    root.rowconfigure(index =0, weight= 1 )
    
root.mainloop()
