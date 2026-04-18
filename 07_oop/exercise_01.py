# Exercise 1 — OOP
# Topic: Class basics
# Difficulty: ⭐

class BankAccount:
    bank_name = "Python Bank"    # class variable
    total_accounts = 0           # class variable

    def __init__(self, owner, balance=0):
        self.owner   = owner     # instance variable
        self.balance = balance   # instance variable
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"Account({self.owner}: ₹{self.balance})"


# Question 1 — Create objects
acc1 = BankAccount("Ayush", 1000)
acc2 = BankAccount("Rahul", 500)

print(acc1.owner)           # Q1a Ayush 
print(acc2.balance)         # Q1b 1000
print(BankAccount.total_accounts)  # Q1c

# Question 2 — Methods
print(acc1.deposit(500))    # Q2a 1500
print(acc1.withdraw(200))   # Q2b 1300
print(acc1.withdraw(5000))  # Q2c Insufficient funds!

# Question 3 — Class vs instance variable
print(acc1.bank_name)       # Q3a "Python Bank"
print(BankAccount.bank_name)# Q3b — same? "Python Bank"

# Question 4 — __str__
print(acc1)                 # Q4 Ayush:1300
print(acc2)                 # Q4b Rahul:500

# Question 5 — Shared class variable
acc3 = BankAccount("Priya", 2000)
print(BankAccount.total_accounts)  # Q5 — how many?3