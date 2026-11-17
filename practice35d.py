class BankAccount:
    def __init__(self):
        self._balance=1000
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,new_balance):
        if new_balance<0:
            print("Error: Balance never be Negative!")
        else:
            self._balance=self._balance
            print("Balance Updated successfully")
a=BankAccount()
a.balance=500
print(a.balance)
