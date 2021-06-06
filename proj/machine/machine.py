from machine.coin import Coin
from machine.coinStorage import coinStore,possibleCoins

from decimal import Decimal
from tkinter import Label as Label

from copy import copy

from tkinter import messagebox


class machine(coinStore):
    """
    equipment is stored as => [[ItemId,price,name,countOfTheProduct],[],[],[],....]
    itemId => item Id
    price => price of the product in 0.01 of the currency(for example if price = 159 tha means it is 1.59 of the currency)
    name => name of the product
    countOfTheProduct => how many items left
    currency => currency of coins used in machine
    change => list of coins in the machine on start for returning change
    """

    def __init__(self, eq: list, currency, change: list):
        super().__init__(currency=currency)
        self.cancelled = False
        self.digitsPicked: list[int] = []
        self.price = Decimal('0.00')
        self.isBuying = False
        self.indexEq = None
        self.insertedCoins = list()
        self.values = change

        if not isinstance(eq, list) and len(eq) != 20:
            raise AttributeError("parameter \"eq\" must of type list of lists [[],[],[]...]")
        elif eq:
            self.eq = eq
        else:  # default
            self.eq = [[itemId, 0, "", 5] for itemId in range(30, 51)]

    def __str__(self):
        return str(self.eq)

    def repr_item(self,numberOfItem:int):
        return "[ id : "+str(self.eq[numberOfItem-30][0])+" | price : "+str(self.eq[numberOfItem-30][1])+" | name : "+str(self.eq[numberOfItem-30][2])+" | count : "+str(self.eq[numberOfItem-30][3])+" ]"

    def changeItemInEq(self, numberOfItem, itemId, price, name, count):
        self.eq[numberOfItem] = [itemId, price, name, count]

    def changeEq(self, eq: list):
        if type(eq) != type(list):
            raise AttributeError("parameter \"eq\" must of type list of lists [[],[],[]...]")
        elif eq:
            self.eq = eq

    def dispenseItem(self):
        self.eq[self.indexEq][3] -= 1
        messagebox.showinfo("dispensing",
                            "dispensing item : " + self.eq[self.indexEq][2] + ", number of items left : " +
                            str(self.eq[self.indexEq][3]))

    def enterDigit(self, digit):
        if len(self.digitsPicked) == 0:
            self.digitsPicked.append(digit)
        elif len(self.digitsPicked) == 1:
            self.digitsPicked.append(digit)
        else:
            return

    def keyboardInputHandler(self, digit, label: Label):
        if len(self.digitsPicked) == 0:
            self.enterDigit(digit)
            self.displayDigits(label)
        elif len(self.digitsPicked) == 1:
            self.enterDigit(digit)
            self.indexEq = 10 * self.digitsPicked[0] + self.digitsPicked[1] - 30
            self.displayDigits(label)
        else:
            return

    def displayDigits(self, label: Label, ):
        if len(self.digitsPicked) == 0:
            label.config(text="00")
        elif len(self.digitsPicked) == 1:
            label.config(text=str(self.digitsPicked[0]))
        elif len(self.digitsPicked) == 2:
            label.config(text=str(self.indexEq + 30))
        else:
            raise Exception("unknown exception")

    def displayAmountToPay(self, label: Label):
        label.config(text=str(self.price))

    def displayPrice(self, label: Label):
        if len(self.digitsPicked) < 2 or self.indexEq is None:
            print("to few digits picked")
            return

        if self.indexEq < 0 or self.indexEq > 20:
            label.config(text="N/A")
            return

        if self.eq[self.indexEq][3] <= 0:
            print("item on this number has been bought up.")
            return
        elif len(self.digitsPicked) == 2:
            label.config(text=str(self.eq[self.indexEq][1]))

    def buy(self, label: Label):
        if len(self.digitsPicked) < 2 or self.indexEq is None:
            print("to few digits picked")
            return

        if self.indexEq < 0 or self.indexEq > 20:
            label.config(text="N/A")
            self.resetAction(label)
            return

        if self.eq[self.indexEq][3] <= 0:
            label.config(text="N/A")
            messagebox.showerror("N/A"," item on this number has been bought up.")
            self.resetAction(label)
            return

        if len(self.digitsPicked) == 2:
            self.displayPrice(label)
            self.isBuying = True
            self.price = Decimal(str(self.eq[self.indexEq][1]))
        else:
            return

    def resetAction(self, label: Label):
        if len(self.digitsPicked) > 0:
            self.digitsPicked.clear()

        self.returnInputtedCoinsIfCanceled()
        self.price = Decimal('0.00')

        self.displayDigits(label)
        self.isBuying = False
        self.indexEq = None
        self.cancelled = False

    def finishTransaction(self, label: Label):


        coinsToReturn = self.returnChangeInCoins()

        if coinsToReturn:
            if isinstance(coinsToReturn[0],Coin):
                messagebox.showinfo("returning", "coins returned:  " + str([float(i.value) for i in coinsToReturn]) )
            else:
                messagebox.showinfo("returning", "coins returned:  None")
            self.values += self.insertedCoins
            self.insertedCoins.clear()
            self.dispenseItem()

            self.digitsPicked.clear()
            self.price = Decimal('0.00')

        else:
            messagebox.showerror("could not return change", "only exact price")
            messagebox.showinfo("returning :","coins returned : [" + str([float(i.value) for i in self.insertedCoins]) + "]")
            self.insertedCoins.clear()

        self.displayDigits(label)
        self.isBuying = False
        self.indexEq = None
        self.cancelled = False

        return

    def returnInputtedCoinsIfCanceled(self):
        messagebox.showinfo("[TRANSACTION_CANCELED]",
                            "\tcoins returned :" + str([float(i.value) for i in self.insertedCoins]))
        if self.insertedCoins:
            self.insertedCoins.clear()

    def inputCoin(self, coin: Coin, label: Label):
        if self.isBuying and self.indexEq is not None:
            self.price -= coin.value
            self.insertedCoins.append(copy(coin))
            self.displayAmountToPay(label)

            if self.price <= 0:
                self.finishTransaction(label)
        else:
            messagebox.showinfo("no input,", "no item selected")
            return

    def returnChangeInCoins(self):
        if self.price < 0:
            change = abs(self.price)
            returnCoins = self.convertDecimalToListOfCoins(change)
        else:
            return [Decimal("0.00")]

        return returnCoins

    def convertDecimalToListOfCoins(self, dec: Decimal):
        coinsToReturnV = []
        coinsToReturnI = []
        inserted = copy(self.insertedCoins)

        for i in possibleCoins:
            if dec > 0:
                while dec >= i.value:
                    #print([float(i.value) for i in self.values])
                    if i in self.values:
                        self.values.remove(i)
                        coinsToReturnV.append(i)
                        dec -= i.value
                    elif i in inserted:
                        inserted.remove(i)
                        coinsToReturnI.append(i)
                        dec -= i.value
                    else:
                        break
            else:
                break

        if dec != 0:
            self.values += coinsToReturnV
            self.insertedCoins += coinsToReturnI
            return False

        return coinsToReturnV+coinsToReturnI
