# Account.py
# Tom Green
# ----------------------------------------------------------------------

from Transactions import *

# ----------------------------------------------------------------------

class Account:

    """represents a bank account """

    # ------------------------------------------------------------------

    def __init__(self, name: str, startingBalance:float=0.0):
        """

        :param name: the name of the account
        :param startingBalance: the starting balance for the account
        """

        self.name = name
        self.balance = startingBalance
        self.transactions = []
        self.balanceHistory = []

    # ------------------------------------------------------------------

    def addTransaction(self, trans: Transaction):

        """
        adds trans to the account's transactions
        :param trans: Transaction to add to the account
        :return: None
        """

        self.transactions.append(trans)
        self.balance += trans._amount()

    # ------------------------------------------------------------------

    def writeToFile(self, filename):

        """
        :param filename: name of file to write account information to
        :return: None
        """

        pass

    # ------------------------------------------------------------------

    @classmethod
    def readFromFile(cls, filename) -> 'Account':

        """
        read account information from the file specified by filename
        :param filename:
        :return: Account object with information from the file
        """

        pass

    # ------------------------------------------------------------------

    def __str__(self) -> str:

        """

        :return: string representation of the account and all its transactions
        first line contains account name followed by a space followed by the starting balance with 2 digits after the decimal
        next line is 78 dashes
        each transaction is written as:
        date is left justified in 11 spaces
        the transaction kind is left justified in 6 spaces
        the description is left justified in 25 spaces
        if the transaction amount is positive, it is right justified in 12 spaces with 2 digits after the decimal followed by 12 spaces
        if the transaction amount is negative, its absolute vlaue is right justified in 24 spaces with 2 digits after the decimal
        the updated current balance is displayed in 12 spaces with 2 digits after the decimal
        each transaction is on its own line and separated by 78 dashes
        """

        print(self.name, self.balance)
        print('-'*78)
        for i in self.transactions:
            print(i._date(), i._name(), i._description(), end=' ')
            amount = i._amount()
            if amount < 0:
                print(amount * -1, end=' ')
            else:
                print(amount, end=' ')
            print(self.balance)
            print('-' * 78)
        return ''

    # ------------------------------------------------------------------

def main():
    a = Account('checking', 1000)
    t = Transaction('06/25/2017', 'D', 'Deposit', 500)
    a.addTransaction(t)
    t = Transaction('06/25/2017', '100', 'AEP', -100)
    a.addTransaction(t)
    a.writeToFile("data.txt")
    print(a)

    #b = Account.readFromFile('data.txt')
    #print()
    #print(b)

if __name__ == '__main__':
    main()


