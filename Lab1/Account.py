#Tom Green
#Lab 1
#Start!

from Transactions import *

class Account:

    def __init__(self):

        self.name = None
        self.balance = 0.0
        self.transactions = []

    def addTransaction(self, t):
        self.transactions.append(t)

    def writeToFile(self, filename):
        break

    def readFromFile(self, filename):
        break

    def __str__(self):
        break