import decimal
import inspect
from pprint import pprint
from machine.coin import *
from machine.machine import *

import math
import random

import tkinter as tk

# tests
from machine.exceptions import *



eq = [[iid + random.randint(10, 200),
       round(random.uniform(1.0, 10.0), 2),
       (chr(random.randint(97, 97 + 26 - 1)) + chr(random.randint(97, 97 + 26 - 1)) + chr(random.randint(97, 97 + 26 - 1))),
       random.randint(2,8)]
      for iid in range(30, 51)]

drinkMachine = machine(eq,"PLN")


root = tk.Tk()

# canvas/grid setup
canvas = tk.Canvas(root, width=800, height=600)
canvas.grid(columnspan=16, rowspan=24)

# buttons setup
keyH = 6
keyW = 14

# KEYBOARD
#0 button
keyboard = [tk.Button(root, textvariable=tk.StringVar(root, "0"), bg="grey", fg="white", height=keyH, width=keyW,
                      command=lambda: drinkMachine.keyboardInputHandler(0,screenLabel))]
keyboard[0].grid(columnspan=1, rowspan=1, column=6, row=4, sticky="NSEW")

#1-9 buttons
for i in range(1, 10):
    keyboard.append(
        tk.Button(root, textvariable=tk.StringVar(root, str(i)), bg="grey", fg="white", height=keyH, width=keyW,
                  command=lambda arg=i: drinkMachine.keyboardInputHandler(arg,screenLabel)))
    keyboard[i].grid(columnspan=1, rowspan=1, column=(i - 1) % 3 + 5, row=(i - 1) // 3, sticky="NSEW")

#Cancel "C"
keyboard.append(tk.Button(root, textvariable=tk.StringVar(root, "C"), bg="grey", fg="white", height=keyH, width=keyW,
                          command=lambda: drinkMachine.transactionCancelled(screenLabel)))
keyboard[10].grid(columnspan=1, rowspan=1, column=5, row=4, sticky="NSEW")

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
coins = [Coin(Decimal('0.01'),"PLN"), Coin(Decimal('0.02'),"PLN"), Coin(Decimal('0.05'),"PLN"),
         Coin(Decimal('0.1'),"PLN"), Coin(Decimal('0.2'),"PLN"), Coin(Decimal('0.5'),"PLN"),
         Coin(Decimal('1'),"PLN"),Coin(Decimal('2'),"PLN"),Coin(Decimal('5'),"PLN")]

print

for i in range(len(coins)):
    coinsBtn.append(
        tk.Button(root, textvariable=tk.StringVar(root, "enter " + str(coins[i].value)), bg="grey", fg="white", height=4,width=14,
                  command=lambda arg=i: drinkMachine.inputCoin(coins[arg],screenLabel)))
    coinsBtn[i].grid(columnspan=1, rowspan=1, column=i % 3, row=1 + 4 + (i // 3), sticky="NSEW")

# LABELS
# SHOW number entered/price of product
screenLabel = tk.Label(root, text="00", fg="red", bg="black", height=1, width=5, font=("Consolas", 80))
screenLabel.grid(columnspan=3, rowspan=3, column=0, row=1)

tk.mainloop()
