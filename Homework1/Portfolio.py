## Here is a python file for Portfolio class
from random import uniform


class Portfolio():

    def __init__(self):
        self.cash = 0
        self.stocks = {}
        self.mutualFunds = {}
        self.transaction_history = []

    def addCash(self, cash):
        self.cash += cash
        transaction_statement = "{:.2f}".format(cash) + "$ were added to the portfolio."
        self.transaction_history.append(transaction_statement)
        print(transaction_statement)

    def withdrawCash(self, cash):
        if self.cash >= cash:
            self.cash -= cash
            transaction_statement = "{:.2f}".format(cash) + "$ were withdrawn from the portfolio."
            self.transaction_history.append(transaction_statement)
            print(transaction_statement)
        else:
            return "You don't have enough cash to withdraw " + cash + "$."

    def buyStock(self, number_of_shares, stock):
        price = stock.price * number_of_shares

        if self.cash >= price:
            self.stocks[stock] = number_of_shares
            self.cash -= price

            tranasaction_statement = "{:.0f}".format(
                number_of_shares) + " shares of " + stock.symbol + " stock were bought"
            self.transaction_history.append(tranasaction_statement)
            print(tranasaction_statement + " with price of {:0.2f}$ per share".format(stock.price))

        else:
            return "You don't have enough cash to buy " + number_of_shares + " shares of this stock."

    def sellStock(self, symbol, number_of_shares):

        for key in self.stocks:

            if key.symbol == symbol and self.stocks[key] >= number_of_shares:

                sell_price = uniform(0.5 * key.price, 1.5 * key.price)
                price = number_of_shares * sell_price
                self.stocks[key] = self.stocks[key] - number_of_shares
                self.cash += price

                transaction_statement = "{:.0f}".format(
                    number_of_shares) + " shares of " + symbol + " stock were sold"
                self.transaction_history.append(transaction_statement)
                print(transaction_statement + " with price of {:0.2f}$ per share".format(sell_price))

            else:
                return "You don't have {:.0f}".format(number_of_shares) + " shares to sell!"

    def buyMutualFund(self, number_of_shares, mutualFund):
        price = number_of_shares * mutualFund.price
        if self.cash >= number_of_shares:
            self.mutualFunds[mutualFund] = number_of_shares
            self.cash -= price
            transaction_statement = "{:.2f}".format(
                number_of_shares) + " shares of " + mutualFund.symbol + " mutual funds were bought."
            self.transaction_history.append(transaction_statement)
            print(transaction_statement + " with price of {:0.2f}$ per share".format(1))
        else:
            return "You don't have enough cash to buy {:.2f}".format(number_of_shares) + " shares of this mutual fund."

    def sellMutualFund(self, symbol, number_of_shares):

        sell_price = uniform(0.9, 1.2)
        price = number_of_shares * sell_price

        for key in self.mutualFunds:
            if key.symbol == symbol and self.mutualFunds[key] >= number_of_shares:

                self.mutualFunds[key] = self.mutualFunds[key] - number_of_shares
                self.cash += price

                transaction_statement = "{:.2f}".format(
                    number_of_shares) + " shares of " + symbol + " mutual funds were sold"
                self.transaction_history.append(transaction_statement)
                print(transaction_statement + " with price of {:0.2f}$ per share".format(sell_price))

            else:
                return "You don't have " + str(number_of_shares) + "to sell!"

    def history(self):
        print("Your Portfolio Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def __str__(self):
        return "Balance: {}. \nStocks: {}\nMutual Funds: {}".format("{:.2f}".format(self.cash), self.stocks,
                                                                        self.mutualFunds)

    def __repr__(self):
        return self.__str__()
