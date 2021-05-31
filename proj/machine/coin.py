from dataclasses import dataclass, field

from decimal import *

@dataclass(frozen=True, order=True)
class Coin:
    """
    value => (Decimal)value of a coin, must be one of : 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5
    currency => str of for example PLN,USD,EUR...etc
    """
    value: Decimal = field(metadata="(Decimal)value of a coin must be one of : 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5")
    currency: str = field(metadata="str of for example PLN,USD,EUR...etc")


    def __post_init__(self):
        if self.value not in {0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5}:
            raise AttributeError("value of a coin must be one of : 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5")


    def __str__(self):
        return "{currency : " + str(self.currency) + ", value : " + str(self.value)

