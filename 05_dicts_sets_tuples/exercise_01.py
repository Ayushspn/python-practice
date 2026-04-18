# Exercise 1 — Dictionaries
# Topic: Dict basics and methods
# Difficulty: ⭐

person = {
    "name": "Ayush",
    "age": 30,
    "city": "Bangalore",
    "skills": ["Python", "React"]
}

# Question 1 — Accessing
print(person["name"])           # Q1a Ayush
print(person.get("age"))        # Q1b 30
print(person.get("salary", 0))  # Q1c — key missing! 0

# Question 2 — Modifying
person["age"] = 31
person["email"] = "ayush@gmail.com"
print(person["age"])            # Q2a 31
print(len(person))              # Q2b — how many keys? 5

# Question 3 — Iterating
for key, value in person.items():
    print(f"{key}: {value}")    # Q3 — what prints? name: Ayush, age: 30, city : Bangalore, skill: ["Python,React"]

# Question 4 — Dict methods
print(list(person.keys()))      # Q4a ["name", "age", "city", "skills"]
print(list(person.values()))    # Q4b ["Ayush", 30, Bangalore, skills]

# Question 5 — Check key exists
print("name" in person)         # Q5a True
print("salary" in person)       # Q5b False

# Question 6 — Remove key
removed = person.pop("city")
print(removed)                  # Q6a — what was removed? Bangalore
print("city" in person)         # Q6b — still there? False