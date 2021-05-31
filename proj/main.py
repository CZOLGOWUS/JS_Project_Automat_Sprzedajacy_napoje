import inspect
from pprint import pprint
from machine.coin import Coin

#tests
from machine.exceptions import *

def main():
    c = Coin(2,"PLN")
    #print(c)
    print([[id,0.0,""] for id in range(30,51)])


if __name__ == "__main__":
    main()
