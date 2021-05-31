from machine.coinStorage import *
from machine.exceptions import *


class machine(coinStore):
    def __init__(self, eq: list):
        if type(eq) != type(list):
            raise AttributeError("parameter \"eq\" must of type list of lists [[],[],[]...]")
        elif eq:
            self.eq = eq
        else:  # default
            self.eq = [[itemId, 0.0, ""] for itemId in range(30, 51)]

    def changeItemInEq(self, numberOfItem, itemId, price, name):
        self.eq[numberOfItem] = [itemId, price, name]

    def changeEq(self, eq: list):
        if type(eq) != type(list):
            raise AttributeError("parameter \"eq\" must of type list of lists [[],[],[]...]")
        elif eq:
            self.eq = eq
