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

    # ------------------------------------------------------------------

    def addTransaction(self, trans: Transaction):

        """
        adds trans to the account's transactions
        :param trans: Transaction to add to the account
        :return: None
        """

        self.transactions.append(trans)

    # ------------------------------------------------------------------

    def writeToFile(self, filename):

        """
        :param filename: name of file to write account information to
        :return: None
        """

        outfile = open(filename, 'w')
        print(self.name + '|' + str(self.balance), file=outfile)
        for i in self.transactions:
            print(i._date() + '|' + i._name() + '|' + i._description() + '|' + str(i._amount()), file=outfile)
        outfile.close()

    # ------------------------------------------------------------------

    @classmethod
    def readFromFile(cls, filename) -> 'Account':

        """
        read account information from the file specified by filename
        :param filename:
        :return: Account object with information from the file
        """

        infile = open(filename, 'r')
        newA = infile.readline()
        newA = newA.split('|')
        newA = Account(newA[0], float(newA[1]))
        trans = infile.readlines()
        for i in trans:
            t = i.split('|')
            t = Transaction(t[0], t[1], t[2], float(t[3]))
            newA.addTransaction(t)
        infile.close()
        return newA



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

        details = []
        details.append(self.name)
        details.append(' {0:0.2f}\n'.format(self.balance))
        runningBalance = self.balance
        for i in self.transactions:
            details.append(('-' * 78) + "\n")
            details.append("{0:<11}{1:<6}{2:<25}".format(i._date(), i._name(), i._description()))
            amount = i._amount()
            runningBalance += amount
            if amount < 0:
                details.append("{0:>24.2f}".format(amount * -1))
            else:
                details.append("{0:>12.2f}            ".format(amount))
            details.append("{0:>12.2f}\n".format(runningBalance))
        details.append('-' * 78)
        details = ''.join(details)
        return details

    # ------------------------------------------------------------------

def main():
    a = Account('checking', 1000)
    t = Transaction('06/25/2017', 'D', 'Deposit', 500)
    a.addTransaction(t)
    t = Transaction('06/25/2017', '100', 'AEP', -100)
    a.addTransaction(t)
    a.writeToFile("data.txt")
    print(a)

    b = Account.readFromFile('data.txt')
    print()
    print(b)

if __name__ == '__main__':
    main()


