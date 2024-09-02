class BalanceException(Exception):
    pass


class BankAccount:
    def __init__ (self, initialAmount,AccountName):
        self.balance = initialAmount
        self.name = AccountName
        print("Account name is {name} and it's balance is {balance}".format(name = self.name, balance = self.balance))

    def getbalance(self):
        print("Balance is {balance}".format(balance = self.balance))
    def deposit(self, Amount):
        self.balance = self.balance + Amount
        self.getbalance()
    def ViableTransaction(self,amount):
        if amount>self.balance:
            raise BalanceException(
                "{Amount} is not enough".format(Amount=self.balance)
            )
        else:
            return
        
    def withdraw(self,amount):
        try:
            self.ViableTransaction(amount)
            self.balance = self.balance - amount
            print("Withdraw compelete")
            self.getbalance()
        except BalanceException as error:
            print("Withdraw Interuppted: {meow}".format (meow = error))

    def transfer(self,amount,account):
     try:
        self.ViableTransaction(amount)
        self.withdraw(amount)
        account.deposit(amount)
     except BalanceException as error:
                     print("Transaction Interuppted: {meow}".format (meow = error))

class InterestReward(BankAccount):
     def deposit(self,amount):
        self.balance = self.balance + (amount*1.05)
        print("Deposit Compelete")
        self.getbalance()
class SavingAccount(InterestReward):
     def __init__(self, initialAmount, AccountName):
          super().__init__(initialAmount,AccountName)
          self.fee = 5
     def withdraw(self,amount):
          try:
               self.ViableTransaction(amount + self.fee)
               self.balance = self.balance - (amount + self.fee)
               print("Withdraw Compelete")
          except BalanceException as error:
               print("Withdraw Interuptted {error}".format(error = error))
     

         
          
     


