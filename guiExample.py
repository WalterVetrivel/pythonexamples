from tkinter import *
from tkinter.ttk import *

OPTIONS = ['Option 1', 'Option 2']


def optionChangeHandler(evt):
    widget = evt.widget
    index = int(widget.curselection()[0])
    value = widget.get(index)

    if value == 'Option 1':
        print('You chose option 1')
        outputVar.set('Option 1')
    else:
        print('You chose option 2')
        outputVar.set('Option 2')


def displayName():
    nameDispLabel['text'] = nameVar.get()


# Defining UI elements
window = Tk()
window.title('Example')

nameLabel = Label(window, text="Enter your name: ")

nameVar = StringVar()
nameEntry = Entry(window, width=10, textvariable=nameVar)

optionsList = Listbox(window)

for option in OPTIONS:
    optionsList.insert(END, option)

optionsList.bind('<<ListboxSelect>>', optionChangeHandler)

outputVar = StringVar()
outputEntry = Entry(window, width=10, state='readonly',
                    textvariable=outputVar)

nameDispLabel = Label(window)
nameDispButton = Button(window, text='Click Me',
                        command=displayName)

# Placing UI elements on window
nameLabel.grid(row=0, column=0)
nameEntry.grid(row=0, column=1)
optionsList.grid(row=1, column=0)
outputEntry.grid(row=1, column=1)
nameDispLabel.grid(row=2, column=0)
nameDispButton.grid(row=2, column=1)

window.mainloop()
