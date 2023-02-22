from tkinter import *
from tkinter import ttk

exercise = ""
number = ""

def resetCalculator():
    global exercise, number
    resultLabel.config(text = "0")
    exercise = ""
    number = ""

def calculate():
    global exercise, number
    result = eval(exercise + number)
    resultLabel.config(text = result)
    exercise = ""
    number = str(result)

def buildNumber(value: str):
    global exercise, number
    if value == "." and "." in number:
        return
    number += value
    result = exercise + number
    resultLabel.config(text = result)

def addOperation(value: str):
    global exercise, number
    exercise += number + value
    number = ""
    resultLabel.config(text = exercise)

def buttonClicked(value: str):
    if value == "=":
        calculate()
    elif value == "AC":
        resetCalculator()
    elif value in digits or value == ".":
        buildNumber(value)
    elif value in operations:
        addOperation(value)

def makeButton(frame: ttk.Frame, value: int):
    return ttk.Button(frame, text=value, command=lambda m=value: buttonClicked(str(value)))

root = Tk()
root.geometry("350x200+200+100")
root.title("CALCULATOR")
frame = ttk.Frame(root, padding = 10)
frame.grid()

resultLabel = ttk.Label(frame, text = "0")
resultLabel.grid(column = 3, row = 0)

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
        button = makeButton(frame, str(value))
        if value == "=":
            button.grid(column = 3, row = rowIndex + 1, sticky = "nswe", padx = 3, pady = 3)
        else:
            button.grid(column = columnIndex, row = rowIndex + 1, sticky = "nswe", padx = 3, pady = 3)

root.mainloop()
