##main module
from Portfolio import Portfolio
from Stock import Stock
from MutualFund import MutualFund


portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
#print(portfolio)
portfolio.sellMutualFund("BRT", 3)
#portfolio.sellStock("HFH", 1)
portfolio.withdrawCash(50)
#portfolio.history()



