# Importing everything from tkinter to avoid typing tkinter. in front of all the GUI elements like buttons and entries
from tkinter import *

# CONSTANTS
ADD = 'add'
SUBTRACT = 'sub'
MULTIPLY = 'mul'


# Function Definitions
# Function to get inputs from the Entries and return them as a list
def getInputs():
    input1 = int(input1TextVariable.get())
    input2 = int(input2TextVariable.get())

    return [input1, input2]


# Function to add two numbers
def addInputs():
    [input1, input2] = getInputs()

    result = input1 + input2

    displayOutput(ADD, result)


# Function to subtract two numbers
def subtractInputs():
    [input1, input2] = getInputs()

    result = input1 - input2

    displayOutput(SUBTRACT, result)


# Function to multiply two numbers
def multiplyInputs():
    [input1, input2] = getInputs()

    result = input1 * input2

    displayOutput(MULTIPLY, result)


# Function to display the output based on which operation was done and the result value
def displayOutput(operation, value):
    if operation == 'add':
        outputTextVariable.set('SUM = ' + str(value))
    elif operation == 'sub':
        outputTextVariable.set('DIFFERENCE = ' + str(value))
    elif operation == 'mul':
        outputTextVariable.set('PRODUCT = ' + str(value))
    else:
        outputTextVariable.set('ERROR. INVALID OPERATION.')


# Creating a window
window = Tk()
window.title('Calculator')

# 2 Labels, 2 Entries for input, 1 read-only Entry for output, 3 Buttons

# LABELS: Label(parentContainer, text)
# ENTRIES: Entry(parentContainer, width, textvariable)
# BUTTONS: Button(parentContainer, text/butonLabel, width, command)

# Labels
input1Label = Label(window, text='First\nNumber')
input2Label = Label(window, text='Second\nNumber')

# Entries
# The text variables store the actual value entered into the entry field
input1TextVariable = StringVar()
input1Entry = Entry(window, width=5, textvariable=input1TextVariable)

input2TextVariable = StringVar()
input2Entry = Entry(window, width=5, textvariable=input2TextVariable)

# Buttons
# The command is the function that needs to be called when the button is clicked
addButton = Button(window, width=3, text='+', command=addInputs)
subtractButton = Button(window, width=3, text='-', command=subtractInputs)
multiplyButton = Button(window, width=3, text='*', command=multiplyInputs)

# Output Entry
outputTextVariable = StringVar()
outputEntry = Entry(window, state='readonly', textvariable=outputTextVariable)

# Positioning elements using grid
input1Label.grid(row=0, column=0)
input2Label.grid(row=0, column=2)

input1Entry.grid(row=1, column=0)
input2Entry.grid(row=1, column=2)

addButton.grid(row=0, column=1)
subtractButton.grid(row=1, column=1)
multiplyButton.grid(row=2, column=1)

outputEntry.grid(row=3, column=0, columnspan=3, padx=40, pady=5)

# Starting the GUI program
window.mainloop()
