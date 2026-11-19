class BankAccount:
    def __init__(self,holder_name,initial_balance):
        self.holder_name=holder_name
        self.initial_balance=initial_balance
    @property
    def balance(self):
        return self.balance
    @balance.setter
    def balance(self,new_balance):
        if new_balance<0:
            print("Error Balance can't be Negative!")
        else:
            self.balance=new_balance
            print("Balance Updated!")
class SavingAccount(BankAccount):
    def __init__(self,holder_name,initial_balance,interest_rate):
        super().__init__(holder_name,initial_balance)
        self.interest_rate=interest_rate
    def add_interest(self):
        interest=(self.balance*self.interest_rate)/100
        self.balance=self.interest_rate+interest
        print(f"Interest of {interest} added. New Balance:{self.balance}")
acc=SavingAccount("Mausam",1000,5)
print(f"Account Holder:{acc.holder_name},Initial Balance:{acc.balance}")
acc.balance=-500
acc.add_interest()