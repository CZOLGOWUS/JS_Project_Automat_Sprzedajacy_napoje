from machine.coin import Coin
from machine.coinStorage import coinStore

from decimal import Decimal
from tkinter import Label as Label

from copy import deepcopy


def convertDecimalToListOfCoins(dec: Decimal):
    coinsToReturn = []
    availableCoins = [Decimal('0.01'), Decimal('0.02'), Decimal('0.05'), Decimal('0.1'), Decimal('0.2'),
                      Decimal('0.5'), Decimal('1'), Decimal('2'), Decimal('5')]
    availableCoins.reverse()

    for i in availableCoins:
        while dec >= i:
            coinsToReturn.append(i)
            dec -= i

    return coinsToReturn


class machine(coinStore):
    """
    equipment is stored as => [[ItemId,price,name,countOfTheProduct],[],[],[],....]
    itemId => item Id
    price => price of the product in 0.01 of the currency(for example if price = 159 tha means it is 1.59 of the currency)
    name => name of the product
    countOfTheProduct => how many items left
    """

    def __init__(self, eq: list, currency):
        super().__init__(currency=currency)
        self.cancelled = False
        self.digitsPicked: list[int] = []
        self.price = Decimal('0.00')
        self.isBuying = False
        self.indexEq = None

        if not isinstance(eq, list) and len(eq) != 20:
            raise AttributeError("parameter \"eq\" must of type list of lists [[],[],[]...]")
        elif eq:
            self.eq = eq
        else:  # default
            self.eq = [[itemId, 0, "", 5] for itemId in range(30, 51)]

    def __str__(self):
        return str(self.eq)

    def changeItemInEq(self, numberOfItem, itemId, price, name, count):
        self.eq[numberOfItem] = [itemId, price, name, count]

    def changeEq(self, eq: list):
        if type(eq) != type(list):
            raise AttributeError("parameter \"eq\" must of type list of lists [[],[],[]...]")
        elif eq:
            self.eq = eq

    def dispenseItem(self):
        self.eq[self.indexEq][3] -= 1
        self.isBuying = False
        print("dispensing " + self.eq[self.indexEq][2], self.eq[self.indexEq][3], "items left")

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

    def resetAction(self, label: Label):
        if len(self.digitsPicked) > 0:
            self.digitsPicked.clear()
        if self.cancelled:
            self.returnInputtedCoins()
        self.price = Decimal('0.00')

        self.displayDigits(label)
        self.isBuying = False
        self.indexEq = None
        self.cancelled = False

    def transactionCancelled(self,label:Label):
        self.cancelled = True
        self.resetAction(label)


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
            self.digitsPicked.clear()

    def buy(self, label: Label):
        if len(self.digitsPicked) < 2 or self.indexEq is None:
            print("to few digits picked")
            return

        if self.indexEq < 0 or self.indexEq > 20:
            label.config(text="N/A")
            return

        if self.eq[self.indexEq][3] <= 0:
            print("item on this number has been bought up.")
            return


        if len(self.digitsPicked) == 2:
            self.displayPrice(label)
            self.isBuying = True
            self.price = Decimal(str(self.eq[self.indexEq][1]))
        else:
            return

    def displayAmountToPay(self, label: Label):
        label.config(text=str(self.price))

    def returnChange(self):
        print("[FLOAT]returning :", abs(self.price))
        return self.price

    def returnInputtedCoins(self):
        print("[TRANSACTION_CANCELED] returning :",self.values)
        if self.values:
            self.values.clear()

    def inputCoin(self, coin: Coin, label: Label):
        if self.isBuying and self.indexEq is not None:
            self.price -= coin.value
            self.values.append(deepcopy(coin))
            self.displayAmountToPay(label)

            if self.price == 0:
                self.dispenseItem()
                self.resetAction(label)
            elif self.price < 0:
                self.dispenseItem()
                self.returnChangeInCoins()
                self.resetAction(label)
            else:
                self.displayAmountToPay(label)
        else:
            print("no item selected")
            return

    def returnChangeInCoins(self):
        if self.price < 0:
            change = abs(self.price)
        else:
            return Decimal('0.00')

        print("[TRANSACTION_FINISHED]returning :",convertDecimalToListOfCoins(change))
