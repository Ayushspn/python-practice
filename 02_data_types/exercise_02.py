# Exercise 2 — Data Types
# Topic: Type conversion and behavior
# Difficulty: ⭐⭐

# Question 1 — What prints?
print(bool(0))        # Q1a FALSE
print(bool(""))       # Q1b FALSE
print(bool([]))       # Q1c FALSE
print(bool(None))     # Q1d FALSE
print(bool("False"))  # Q1e — TRUE
print(bool([0]))      # Q1f — TRUE

# Question 2 — What prints?
print(True + True)    # Q2a 2
print(True * 5)       # Q2b 5
print(False + 1)      # Q2c 1

# Question 3 — What prints?
x = "123"
y = int(x)
print(y + 1)          # Q3a 124
print(type(y))        # Q3b int

# Question 4 — What raises error?
try:
    x = int("hello")
except ValueError as e:
    print("ValueError!")   # Q4 can not convert string to int

# Question 5 — What prints?
print(type(10 / 2))   # Q5a — int or float? float
print(type(10 // 2))  # Q5b — int or float? int