
class bank:  
    def __init__(self):
        self.balance = 0
        print("This is your bank account")

    def deposit(self):
        amount = float(input("Enter the amount you would like to be deposited into your account: "))
        money = self.balance + amount
        print("You have £", money, " in your bank account.")
        self.balance = money

    def withdraw(self):
        amount = float(input("Enter how much you would like to withdraw from your bank account "))
        if amount > self.balance:
                print("Insufficient money")
        elif amount < self.balance:
            money = self.balance - amount
            print("You are now left with £", money)
            interest = 0.05
            year = float(input("How many years have you left your bank account "))
            total = money * interest * year
            money1 = total + money
            print("After", year, "years, you now have £", money1)




s = bank()
s.deposit()
s.withdraw()
