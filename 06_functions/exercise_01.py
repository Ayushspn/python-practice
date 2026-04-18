# Exercise 1 — Functions
# Topic: Args, kwargs, defaults
# Difficulty: ⭐

# Question 1 — Basic function
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ayush"))           # Q1a Hello, Ayush
print(greet("Rahul", "Hi"))     # Q1b Hi, Rahul
print(greet(greeting="Namaste", name="Priya"))  # Q1c Namste, Priya

# Question 2 — *args
def total(*args):
    return sum(args)

print(total(1, 2, 3))           # Q2a 6
print(total(1, 2, 3, 4, 5))     # Q2b 15
##print(type(args))               # Q2c — what type is args?

# Question 3 — **kwargs
def display(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display(name="Ayush", age=30, city="Bangalore")  # Q3

# Question 4 — Combined
def mixed(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

mixed(1, 2, 3, 4, name="Ayush")  # Q4 a=1, b=2 args = (3,4), kwargs= {"name": "Ayush"}

# Question 5 — Return multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 9, 5, 2])
print(low)      # Q5a 1
print(high)     # Q5b 9