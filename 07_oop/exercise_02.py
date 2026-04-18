# Exercise 2 — OOP
# Topic: Inheritance
# Difficulty: ⭐⭐

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} is {self.age} years old"

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):           # override!
        return "Woof!"

    def fetch(self):           # new method
        return f"{self.name} fetches the ball!"


class Cat(Animal):
    def speak(self):           # override!
        return "Meow!"


# Question 1 — Basic inheritance
dog = Dog("Bruno", 3, "Labrador")
cat = Cat("Whiskers", 2)

print(dog.speak())      # Q1a
print(cat.speak())      # Q1b
print(dog.describe())   # Q1c — inherited from Animal!
print(dog.fetch())      # Q1d

# Question 2 — isinstance
print(isinstance(dog, Dog))     # Q2a
print(isinstance(dog, Animal))  # Q2b — True or False?
print(isinstance(cat, Dog))     # Q2c

# Question 3 — __str__
print(dog)   # Q3a
print(cat)   # Q3b

# Question 4 — super()
class GoldenRetriever(Dog):
    def __init__(self, name, age):
        super().__init__(name, age, "Golden Retriever")

    def speak(self):
        parent = super().speak()
        return f"{parent} {parent}"   # double woof!

gr = GoldenRetriever("Max", 2)
print(gr.speak())       # Q4a
print(gr.breed)         # Q4b
print(gr.describe())    # Q4c