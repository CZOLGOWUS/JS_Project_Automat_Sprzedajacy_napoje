
class CoinStoreIsNotEmptyException(Exception):
    def __init__(self, msg):
        self.msg = msg

class ItemNotAvailableException(Exception):
    def __init__(self, msg):
        self.msg = msg
