from Project1 import *

Aryan = BankAccount(5000,"Aryan")
print(Aryan.balance)
Aryan.deposit(5000)
Aryan.withdraw(300000)
Blaze = SavingAccount(69, "Blaze")
Blaze.getbalance()
Blaze.deposit(100)
Blaze.transfer(1000, Aryan)
