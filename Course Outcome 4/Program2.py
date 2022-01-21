class BankAccount:
    def __init__(self,name):
        self.name=name
        self.balance=0.0
        print("\n",self.name,"'s Account created successfully!")
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
user1=BankAccount("Gokul")
user1.balanceDisplay()
user1.deposit()
user1.withdraw()
user2=BankAccount("Nikhil")
user2.balanceDisplay()
user2.deposit()
user2.withdraw()