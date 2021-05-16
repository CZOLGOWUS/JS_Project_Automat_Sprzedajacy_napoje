import inspect
from pprint import pprint

import numpy as np
from dataclasses import dataclass, field


@dataclass(frozen=True,order=True)
class Coin:
    value: float = field(metadata="value of a coin must be one of : 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5")
    curr: str = field(metadata="str of for example PLN,USD,EUR...etc")

    def __post_init__(self):
        if self.value not in {0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5}:
            raise AttributeError("value of a coin must be one of : 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5")

def main():
    c = Coin(2,"PLN")
    print(c)

    pprint(inspect.getmembers(Coin,inspect.isfunction))


if __name__ == "__main__":
    main()
