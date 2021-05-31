import inspect
from pprint import pprint
from machine.coin import Coin
import tkinter as tk

# tests
from machine.exceptions import *


#
# def test():
#     c = Coin(0.5,"PLN")
#     print(c)
#     #print([[id,0.0,""] for id in range(30,51)])
#
#
#
# if __name__ == "__main__":
#        test()

def test():
    print("test")


root = tk.Tk()

# canvas/grid setup
canvas = tk.Canvas(root, width=800, height=600)
canvas.grid(columnspan=8, rowspan=10)

# buttons setup
keyH = 6
keyW = 14



#KEYBOARD
keyboard = [
    tk.Button(root,
              textvariable=tk.StringVar(root, "0"),
              bg="grey",
              fg="white",
              height=keyH,
              width=keyW,
              command=lambda: test())
]
keyboard[0].grid(columnspan=1, rowspan=1, column=6, row=4)

for i in range(1, 10):
    keyboard.append(tk.Button(root,
                              textvariable=tk.StringVar(root, str(i)),
                              bg="grey",
                              fg="white",
                              height=keyH,
                              width=keyW,
                              command=lambda: test())
                    )
    keyboard[i].grid(columnspan=1, rowspan=1, column=(i - 1) % 3 + 5, row=(i - 1) // 3)

keyboard.append(tk.Button(root,
                          textvariable=tk.StringVar(root, "C"),
                          bg="grey",
                          fg="white",
                          height=keyH,
                          width=keyW,
                          command=lambda: test())
                )
keyboard[10].grid(columnspan=1, rowspan=1, column=5, row=4)



#BUTTONS
buyBtn = tk.Button(root,
                   textvariable=tk.StringVar(root, "buy"),
                   bg="grey",
                   fg="white",
                   height=5,
                   width=15,
                   command=lambda: test())
buyBtn.grid(columnspan=1, rowspan=1, column=1, row=0)



priceBtn = tk.Button(root,
                     textvariable=tk.StringVar(root, "check price"),
                     bg="grey",
                     fg="white",
                     height=5,
                     width=15,
                     command=lambda: test())
priceBtn.grid(columnspan=1, column=0, row=0)


screenLabel = tk.Label(
    root,
    text="00.00",
    fg="red",
    bg="black",
    height=1,
    width=5,
    font=("Consolas",80)

)
screenLabel.grid(columnspan=4,rowspan=2, column=0, row=4)



tk.mainloop()
