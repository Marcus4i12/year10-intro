class bank():
    def __init__(self):
        self.bank_account = 0
        print("This is your bank account")

    def deposit(self, deposit):
        self.bank_account += deposit
        print("You now have £", self.bank_account, "inside your account")

    def withdraw(self, withdraw):
        if self.bank_account < withdraw:
            print("Insufficient funds")
        elif self.bank_account > withdraw:
            self.bank_account -= withdraw
            print("You now have £", self.bank_account)

    def increment_year(self, years):
            interest_rate = 0.05
            self.compound_interest = self.bank_account * ((1 + interest_rate / 1) ** years)
            self.bank_account = self.compound_interest
            print("After", years, "years, you how have £", self.bank_account)

s = bank()
s.deposit(int(input("How much would you like deposited into your account? ")))
s.withdraw(int(input("How much would you like to withdraw from your account? ")))
s.increment_year(int(input("How many years would you like to leave your bank account? " )))