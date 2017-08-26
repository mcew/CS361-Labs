#Transactions
#Tom Green
#Begin!

class Transaction:

    def __init__(self):

        self.date = None
        self.name = None
        self.type = None
        self.amount = 0.0

    def _amount(self):
        return self.amount

    def _date(self):
        return self.date

    def _name(self):
        return self.name

    def _type(self):
        return self.type