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
    result = eval(exercise + number)
    setEntryText(resultOutput, result)
    exercise = ""
    number = str(result)

def buildNumber(value: str):
    global exercise, number
    if value == "." and "." in number:
        return
    number += value
    result = exercise + number
    setEntryText(resultOutput, result)

def addOperation(value: str):
    global exercise, number
    exercise += number + value
    number = ""
    setEntryText(resultOutput, exercise)
    
def setEntryText(entry, text):
    entry.config(state="normal")
    entry.delete(0, END)
    entry.insert(0, text)
    entry.config(state="readonly")

def buttonClicked(value: str):
    if value == "=":
        calculate()
    elif value == "AC":
        resetCalculator()
    elif value in digits or value == ".":
        buildNumber(value)
    elif value in operations and number:
        addOperation(value)

def makeButton(parent, value: str):
    return Button(parent, text=value, font ='areal 15 bold', command=lambda m=value: buttonClicked(value))

root = Tk()
root.geometry("450x400+300+100")
root.title("CALCULATOR")
resultOutput = Entry(root, justify=RIGHT, font ='areal 15 bold', state= "disabled")
setEntryText(resultOutput, "0")
resultOutput.insert(0, '0' )
resultOutput.grid(column = 0, row = 0, columnspan=4, sticky = "nswe",padx = 3, pady = 3)

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
operations = ["+", "-", "*", "/"]
buttonValues = [
    [7, 8, 9, "+"],
    [4, 5, 6, "-"],
    [1, 2, 3, "*"],
    [0, ".","AC", "/"],
    ["="]
]

for rowIndex, row in enumerate(buttonValues):
    for columnIndex, value in enumerate(row):
        button = makeButton(root, str(value))
        if value == "=":
            button.grid(column = 3, row = rowIndex + 1, sticky = "nswe", padx = 3, pady = 3)
        else:
            button.grid(column = columnIndex, row = rowIndex + 1, sticky = "nswe", padx = 3)

        root.columnconfigure(index = columnIndex , weight= 1)
    root.rowconfigure(index = rowIndex + 1, weight= 1 )
    root.rowconfigure(index =0, weight= 1 )
    
root.mainloop()
