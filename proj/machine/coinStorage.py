from dataclasses import dataclass, field

from machine.exceptions import *

@dataclass(order=True)
class coinStore:
    currency: str = field()
    values: list = field()

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
            raise CoinStoreIsNotEmptyException("Storage is not empty")


