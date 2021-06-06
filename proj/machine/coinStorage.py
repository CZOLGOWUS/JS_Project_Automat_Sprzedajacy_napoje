from dataclasses import dataclass, field

from decimal import Decimal

from machine.coin import Coin

possibleCoins = [Coin(Decimal('0.01'), "PLN"), Coin(Decimal('0.02'), "PLN"), Coin(Decimal('0.05'), "PLN"),
                 Coin(Decimal('0.10'), "PLN"), Coin(Decimal('0.20'), "PLN"), Coin(Decimal('0.50'), "PLN"),
                 Coin(Decimal('1.00'), "PLN"), Coin(Decimal('2.00'), "PLN"), Coin(Decimal('5.00'), "PLN")]


@dataclass(order=True)
class coinStore:
    values: list = field(default_factory=list)
    currency: str = field(default="PLN")

    def add(self, coin):
        if coin.currency == self.currency:
            self.values.append(coin)

    def emptyCoins(self):
        c = self.currency
        v = self.values
        self.values.clear()
        return c, v

    def changeCurrency(self, currency: str):
        if len(self.values) == 0:
            self.currency = currency
        else:
            raise Exception("storage is not empty")
