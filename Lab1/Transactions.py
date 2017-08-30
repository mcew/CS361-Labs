#Transactions
#Tom Green
#Begin!

class Transaction:

    def __init__(self, date:str, name:str, description:str, amount:float):

        self.date = date
        self.name = name
        self.description = description
        self.amount = amount

    def _amount(self):
        return self.amount

    def _date(self):
        return self.date

    def _name(self):
        return self.name

    def _description(self):
        return self.description