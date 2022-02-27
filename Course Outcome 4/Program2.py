class BankAccount:
    def __init__(self,accno,name,acctype):
        self.accno=accno
        self.name=name
        self.acctype=acctype
        self.balance=0.0
    def deposit(self):
        self.dAmount=float(input("\nEnter the amount you want to deposit: "))
        self.balance+=self.dAmount
        print("\nRs.",self.dAmount, " is deposited to your account.")
        print("\nYour current balance is Rs.",self.balance)
    def withdraw(self):
        self.wAmount=float(input("\nEnter the amount you want to withdraw: "))
        if self.balance<self.wAmount:
            print("\nInsufficent Balance, the entered amount can't be withdrawed from your account!")
        else:
            self.balance-=self.wAmount
            print("\nRs.",self.wAmount," withdrawed from your account.")
            print("\nYour current balance is Rs.",self.balance)
    def balanceDisplay(self):
        print("\nYour current balance is Rs.",self.balance)
accno=input("Enter the account number: ")
username=input("Enter the name: ")
acctype=input("Enter the account type: ")
user=BankAccount(accno,username,acctype)
user.balanceDisplay()
user.deposit()
user.withdraw()