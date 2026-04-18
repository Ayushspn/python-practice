# Exercise 1 — Strings
# Topic: Indexing and Slicing
# Difficulty: ⭐

name = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5   forward
#      -6 -5 -4 -3 -2 -1   backward

# Question 1 — Basic indexing
print(name[0])      # Q1a p
print(name[-1])     # Q1b n
print(name[2])      # Q1c t

# Question 2 — Slicing
print(name[0:3])    # Q2a p y t
print(name[2:])     # Q2b t  h  o  n
print(name[:4])     # Q2c P  y  t  h  o
print(name[-3:])    # Q2d 3  4  5
print(name[::2])    # Q2e — every 2nd char y h n
print(name[::-1])   # Q2f — reversed! n o h t y P

# Question 3 — String is immutable
name[0] = "J"       # Q3: works or error? error

# Question 4 — What prints?
s = "hello world"
print(s.upper())    # Q4a HELLO WORLD
print(s.replace("world", "Python"))  # Q4b hello Python
print(s)            # Q4c — original changed? no