# Exercise 1 — Data Types
# Topic: Mutable vs Immutable
# Difficulty: ⭐

# Question 1 — which are mutable?
# Write M (mutable) or I (immutable) next to each:

x = 42          # Q1a: M or I? I 
y = "hello"     # Q1b: M or I? I 
z = [1, 2, 3]   # Q1c: M or I? M
a = (1, 2, 3)   # Q1d: M or I? I
b = {"a": 1}    # Q1e: M or I? M
c = {1, 2, 3}   # Q1f: M or I? M

# Question 2 — What prints?
s = "hello"
s.upper()
print(s)        # Q2: "hello" or "HELLO"? hello

# Question 3 — What prints?
s = "hello"
s = s.upper()
print(s)        # Q3: "hello" or "HELLO"? HELLO

# Question 4 — What prints?
lst = [1, 2, 3]
lst.append(4)
print(lst)      # Q4: [1,2,3] or [1,2,3,4]? [1,2,3,4]

# Question 5 — What prints?
t = (1, 2, 3)
try:
    t[0] = 99
except TypeError as e:
    print("Error!")   # Q5: prints "Error!" or works fine? "Error"