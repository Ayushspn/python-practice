# Exercise 1 — Variables & References
# Topic: Reference vs Copy
# Difficulty: ⭐

# Question 1
x = [1, 2, 3]
y = x
y.append(4)
print(x)        # Q1: what prints?

# [1,2,3,4]

# Question 2
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)        # Q2: what prints?

# [1,2,3]

# Question 3
x = 10
y = x
x = 20
print(y)        # Q3: what prints?

#10

# Question 4
name = "Ayush"
name2 = name
name = "Rahul"
print(name2)    # Q4: what prints?

# Ayush