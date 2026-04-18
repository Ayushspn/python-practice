# Exercise 1 — Lists
# Topic: List basics and methods
# Difficulty: ⭐

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Question 1 — Basic operations
print(numbers[0])       # Q1a 3
print(numbers[-1])      # Q1b 6
print(len(numbers))     # Q1c 8
print(numbers[2:5])     # Q1d [4, 1, 5]

# Question 2 — Methods
numbers.append(7)
print(numbers)          # Q2a  [3, 1, 4, 1, 5, 9, 2, 6,7]

numbers.insert(0, 99)
print(numbers)          # Q2b  [99,3, 1, 4, 1, 5, 9, 2, 6,7]

numbers.pop()
print(numbers)          # Q2c [99,3, 1, 4, 1, 5, 9, 2, 6,7]

numbers.remove(1)       # removes FIRST occurrence!
print(numbers)          # Q2d [99,3, 4, 1, 5, 9, 2, 6,7]

# Question 3 — Sorting
nums = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_nums = sorted(nums)
print(sorted_nums)      # Q3a [1, 1, 2, 3, 4, 5, 6, 9]
print(nums)             # Q3b — original changed? [3, 1, 4, 1, 5, 9, 2, 6]

nums.sort()
print(nums)             # Q3c — original changed now? [1, 1, 2, 3, 4, 5, 6, 9]

# Question 4 — Count and index
nums = [3, 1, 4, 1, 5, 9, 2, 6, 1]
print(nums.count(1))    # Q4a 3
print(nums.index(5))    # Q4b — index of 5? 4