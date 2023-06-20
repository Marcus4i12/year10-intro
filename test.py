class bank():
    bank_account = 0
    print("This is your bank account")

    def deposit(self):
        self.deposit = float(input("How much would you like deposited into your account? "))
        self.bank_account += self.deposit
        print("You now have £", self.bank_account, "inside your account")

    def withdraw(self):
        self.withdraw = float(input("How much would you like to withdraw from your account? "))
        if self.bank_account < self.withdraw:
            print("Insufficient funds")
        elif self.bank_account > self.withdraw:
            self.bank_account -= self.withdraw
            print("You now have £", self.bank_account)
    def increment_year(self):
            interest_rate = 0.05
            years = float(input("How many years would you like to leave your bank account? " ))
            self.compound_interest = self.bank_account * ((1 + interest_rate / 1) ** years)
            self.bank_account = self.compound_interest
            print("After", years, "years, you how have £", self.bank_account)




s = bank()
s.deposit()
s.withdraw()
s.increment_year()