# Exercise 2 — Functions
# Topic: Scope and Closures
# Difficulty: ⭐⭐

# Question 1 — LEGB scope
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)      # Q1a — which x? local

    inner()
    print(x)          # Q1b — which x? enclosing

outer()
print(x)              # Q1c — which x? global

# Question 2 — global keyword
count = 0

def increment():
    global count
    count += 1

increment()
increment()
increment()
print(count)          # Q2 — what prints? 3

# Question 3 — Closure
def make_multiplier(n):
    def multiplier(x):
        return x * n    # n captured from outer!
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))      # Q3a 10
print(triple(5))      # Q3b 15
print(double(10))     # Q3c 20

# Question 4 — Closure counter
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
print(counter())      # Q4a 1
print(counter())      # Q4b 2
print(counter())      # Q4c 3

counter2 = make_counter()
print(counter2())     # Q4d — independent counter? 1