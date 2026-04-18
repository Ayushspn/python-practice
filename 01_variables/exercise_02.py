# Exercise 2 — Variables & References
# Topic: id() and memory
# Difficulty: ⭐⭐

# Question 1 — same object or different?
a = 100
b = 100
print(a is b)     # Q1: True or False?

## True

# Question 2 — same object or different?
a = 1000
b = 1000
print(a is b)     # Q2: True or False?

##False

# Question 3 — what happens to id?
x = [1, 2, 3]
print(id(x))      # some number
x.append(4)
print(id(x))      # Q3: same or different id?

##same 

# Question 4 — what happens to id?
x = [1, 2, 3]
print(id(x))      # some number
x = [1, 2, 3, 4]
print(id(x))      # Q4: same or different id?

##different

# Question 5 — tricky!
def add(items, item=[]):
    item.append(items)
    return item

print(add(1))     # Q5a: what prints?
print(add(2))     # Q5b: what prints?
print(add(3))     # Q5c: what prints?

print(add(1))   ## [1]
print(add(2))   # [1,2]
print(add(3))  #[1,2,3]