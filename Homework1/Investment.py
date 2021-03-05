## Investment is a super class.


class Investment():

    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol


    def __str__(self):
        return "Ticker Symbol: " + self.symbol

    def __repr__(self):
        return self.__str__()
