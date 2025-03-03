class BankAccount:
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder
    def __str__(self):
        return f"ID: {self.account_number} Balance: {self.balance} Name: {self.account_holder} "
    def deposit(self,value):
        if value >= 0:
            self.balance += value
        else:
            print("The value cannot be added, it is less than 0")
    def withdrawl(self,withdrawl):
        if withdrawl > self.balance:
            print("The value is to big to be used, as it equals more than the total balance.")
        else:
            self.balance -= withdrawl

customer1 = BankAccount(input("ID "),int(input("Balance ")),input("Account holder "))
customer2 = BankAccount(input("ID "),int(input("Balance ")),input("Account holder "))
customer3 = BankAccount(input("ID "),int(input("Balance ")),input("Account holder "))

customer_list = [customer1,customer2,customer3]
for index in customer_list:
    index.deposit(int(input(f"Enter how much you want to deposit into {index.account_holder}'s account: ")))
    index.withdrawl(int(input(f"Enter how much you want to withdrawl from {index.account_holder}'s account: ")))
    print(index)