# Exercise 2 — Lists
# Topic: List comprehensions
# Difficulty: ⭐⭐

# Question 1 — Basic comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)          # Q1 [2,4,6,8,10]

# Question 2 — With condition
evens = [x for x in range(20) if x % 2 == 0]
print(evens)            # Q2 [0,2,4,6,8,10,12,14,16,18]

# Question 3 — Transform strings
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(upper)            # Q3 ["HELLO", WORLD, PYTHON]

# Question 4 — Nested comprehension
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)             # Q4 [1,2,3,4,5,6,7,8,9]

# Question 5 — Real world
scores = [45, 82, 91, 38, 76, 55, 67]
passed = [s for s in scores if s >= 60]
failed = [s for s in scores if s < 60]
print(passed)           # Q5a [82,91,76,67]
print(failed)           # Q5b [45,38,55]
print(len(passed))      # Q5c 4