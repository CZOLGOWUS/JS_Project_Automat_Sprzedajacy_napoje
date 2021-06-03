
class CoinStoreIsNotEmptyException(Exception):
    def __init__(self, msg):
        self.msg = msg

class ItemNotInStoreException(Exception):
    def __init__(self,msg):
        self.msg = msg

