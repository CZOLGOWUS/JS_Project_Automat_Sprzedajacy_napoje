from dataclasses import dataclass, field

import decimal

from machine.exceptions import *


@dataclass(order=True)
class coinStore:
    values: list = field(default_factory=list)
    currency: str = field(default="PLN")



    def add(self,coin):
        if coin.currency == self.currency:
            self.values.append(coin)

    def emptyCoins(self):
        c = self.currency
        v = self.values
        self.values.clear()
        return c,v

    def changeCurrency(self,currency:str):
        if len(self.values) == 0:
            self.currency = currency
        else:
            raise ItemNotAvailableException("Storage is not empty")


