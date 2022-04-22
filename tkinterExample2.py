from tkinter import *


def findDiscountedTotalPrice():
    prices = [float(itemVar.get()) for itemVar in itemStringVars]
    discountedItem = min(prices)
    print(discountedItem)

    prices.remove(discountedItem)
    print(sum(prices))


window = Tk()

itemStringVars = [StringVar(), StringVar(), StringVar()]

for i in range(0, 3):
    label = Label(window, text=f'Item #{i + 1} price: ')
    label.grid(row=i, column=0)

for i in range(0, 3):
    entry = Entry(window, width=10, textvariable=itemStringVars[i])
    entry.grid(row=i, column=1)

calculateButton = Button(window, text='Calculate',
                         command=findDiscountedTotalPrice)
calculateButton.grid(row=3, column=0)

window.mainloop()
