from machine.machine import *
from machine.coinStorage import possibleCoins

import random
import tkinter as tk
from time import sleep


def test(m:machine,l:Label):

    messagebox.showinfo("price display","price of item with number: 33")
    m.keyboardInputHandler(3,l)
    m.keyboardInputHandler(3,l)
    m.displayPrice(l)
    sleep(1)
    messagebox.showinfo("information about item","item on number 33 = " + m.repr_item(33))
    sleep(1)

    messagebox.showinfo("buying", "buying item with number: 33(item:"+m.repr_item(33)+") by inserting only 0.01 coins (coins inputted in displayed in terminal after transaction)")
    m.buy(l)

    testCoinsList = []
    while m.price > 0:
        testCoinsList.append(str(possibleCoins[8].value))
        m.inputCoin(possibleCoins[8],l)

    print(testCoinsList)
    testCoinsList.clear()


    while m.price > 0:
        testCoinsList.append(str(possibleCoins[0].value))
        m.inputCoin(possibleCoins[0],l)

    print(testCoinsList)


    m.eq[0][3] = 0
    m.keyboardInputHandler(3,l)
    m.keyboardInputHandler(0,l)
    messagebox.showinfo("buying not available item", "trying to buy item out of stock( item on number 30  (item:"+m.repr_item(30)+"))")
    m.buy(l)

    messagebox.showinfo("trying out of bounds numbers", "trying to buy items 25 ")
    m.keyboardInputHandler(2,l)
    m.keyboardInputHandler(5,l)
    m.buy(l)
    sleep(1)

    messagebox.showinfo("trying out of bounds numbers", "trying to buy items 80 ")
    m.keyboardInputHandler(8,l)
    m.keyboardInputHandler(0,l)
    m.buy(l)
    sleep(1)


    messagebox.showinfo("buy and cancel","starting buying proces of item 35(item:"+m.repr_item(35)+") and canceling after inserting 2 coins with 0.2 value")
    m.keyboardInputHandler(3,l)
    m.keyboardInputHandler(5,l)
    m.buy(l)

    testCoinsList.clear()
    for i in range(2):
        testCoinsList.append(str(possibleCoins[4].value))
        m.inputCoin(possibleCoins[4],l)
    print("coins inserted :",testCoinsList)
    m.resetAction(l)



    m.keyboardInputHandler(3,l)
    m.keyboardInputHandler(8,l)
    m.buy(l)
    messagebox.showinfo("buying","buying item with number: 38(price:"+str(m.price)+") by inserting only 0.01 coins (coins inputted in displayed in terminal after transaction)")

    testCoinsList = []
    sumOfInsertedCoins = Decimal("0.00")
    while m.price > 0:
        testCoinsList.append(str(possibleCoins[8].value))
        sumOfInsertedCoins += possibleCoins[8].value
        m.inputCoin(possibleCoins[8], l)

    print(testCoinsList)
    print("sum of all the coins inserted : ",sumOfInsertedCoins)
    testCoinsList.clear()


possibleCoins.reverse()
eq = [[iid + random.randint(10, 200),
       round(random.uniform(1.0, 10.0), 2),
       (chr(random.randint(97, 97 + 26 - 1)) + chr(random.randint(97, 97 + 26 - 1)) + chr(
           random.randint(97, 97 + 26 - 1))),
       random.randint(2, 8)]
      for iid in range(30, 51)]

drinkMachine = machine(
    eq,
    "PLN",
    1 * possibleCoins
)

root = tk.Tk()

# canvas/grid setup
canvas = tk.Canvas(root, width=800, height=600)
canvas.grid(columnspan=16, rowspan=24)

# buttons setup
keyH = 6
keyW = 14

# KEYBOARD
# 0 button
keyboard = [tk.Button(root, textvariable=tk.StringVar(root, "0"), bg="grey", fg="white", height=keyH, width=keyW,
                      command=lambda: drinkMachine.keyboardInputHandler(0, screenLabel))]
keyboard[0].grid(columnspan=1, rowspan=1, column=14, row=4, sticky="NSEW")

# 1-9 buttons
for i in range(1, 10):
    keyboard.append(
        tk.Button(root, textvariable=tk.StringVar(root, str(i)), bg="grey", fg="white", height=keyH, width=keyW,
                  command=lambda arg=i: drinkMachine.keyboardInputHandler(arg, screenLabel)))
    keyboard[i].grid(columnspan=1, rowspan=1, column=(i - 1) % 3 + 13, row=(i - 1) // 3, sticky="NSEW")

# Cancel "C"
keyboard.append(tk.Button(root, textvariable=tk.StringVar(root, "C"), bg="grey", fg="white", height=keyH, width=keyW,
                          command=lambda: drinkMachine.resetAction(screenLabel)))
keyboard[10].grid(columnspan=1, rowspan=1, column=13, row=4, sticky="NSEW")

# BUTTONS
# BUY
buyBtn = tk.Button(root, textvariable=tk.StringVar(root, "buy"), bg="grey", fg="white", height=5, width=15,
                   command=lambda: drinkMachine.buy(screenLabel))
buyBtn.grid(columnspan=1, rowspan=1, column=1, row=0, sticky="NSEW")

# SHOW PRICE
priceBtn = tk.Button(root, textvariable=tk.StringVar(root, "check price"), bg="grey", fg="white", height=5, width=15,
                     command=lambda: drinkMachine.displayPrice(screenLabel))
priceBtn.grid(columnspan=1, column=0, row=0, sticky="NSEW")

# ENTER COINS

coinsBtn = []

for i in range(len(possibleCoins)):
    coinsBtn.append(
        tk.Button(root, textvariable=tk.StringVar(root, "enter " + str(possibleCoins[len(possibleCoins)-1-i].value)), bg="grey", fg="white", height=4, width=14,
                  command=lambda arg=i: drinkMachine.inputCoin(possibleCoins[len(possibleCoins) - 1 - arg], screenLabel)))
    coinsBtn[i].grid(columnspan=1, rowspan=1, column=i % 3, row=1 + 4 + (i // 3), sticky="NSEW")

# LABELS
# SHOW number entered/price of product
screenLabel = tk.Label(root, text="00", fg="red", bg="black", height=1, width=5, font=("Consolas", 80))
screenLabel.grid(columnspan=3, rowspan=3, column=0, row=1)

# TEST BUTTON
priceBtn = tk.Button(root, textvariable=tk.StringVar(root, "TEST"), bg="#82FF7D", fg="black", height=5, width=15,
                     command=lambda: test(drinkMachine,screenLabel))
priceBtn.grid(columnspan=1, column=15, row=7, sticky="NSEW")

tk.mainloop()
