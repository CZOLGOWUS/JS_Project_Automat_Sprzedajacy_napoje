from machine.coinStorage import *
from machine.exceptions import *


class machine(coinStore):
    """
    equipment is stored as => [[ItemId,price,name,countOfTheProduct],[],[],[],....]
    itemId => item Id
    price => price of the product in 0.01 of the currency(for example if price = 159 tha means it is 1.59 of the currency)
    name => name of the product
    countOfTheProduct => how many items left
    """
    def __init__(self, eq: list):
        if type(eq) != type(list):
            raise AttributeError("parameter \"eq\" must of type list of lists [[],[],[]...]")
        elif eq:
            self.eq = eq
        else:  # default
            self.eq = [[itemId, 0, "",5] for itemId in range(30, 51)]

    def changeItemInEq(self, numberOfItem, itemId, price, name,count):
        self.eq[numberOfItem] = [itemId, price, name,count]

    def changeEq(self, eq: list):
        if type(eq) != type(list):
            raise AttributeError("parameter \"eq\" must of type list of lists [[],[],[]...]")
        elif eq:
            self.eq = eq

    def dispenseItem(self, number):
        if self.eq[number][3] <= 0:
            raise ItemNotAvailableException("item on this number has been bought up.")
        else:
            self.eq[number][5] -= 1
            print("dispensing " + self.eq[number][2])

