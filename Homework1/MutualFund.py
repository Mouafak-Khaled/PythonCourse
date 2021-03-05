## mutualFund class
from Investment import Investment


class MutualFund(Investment):

    def __init__(self, symbol):
        super().__init__(1, symbol)
