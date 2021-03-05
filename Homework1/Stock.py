## Stock class
from Investment import Investment

class Stock(Investment):
  
  def __init__(self, price, symbol):
    super().__init__(price, symbol)

