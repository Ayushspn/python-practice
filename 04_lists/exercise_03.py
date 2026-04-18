# Exercise 3 — Lists
# Topic: Real world list operations
# Difficulty: ⭐⭐⭐

# Scenario: Student grade management system

students = [
    {"name": "Ayush",  "score": 95},
    {"name": "Rahul",  "score": 72},
    {"name": "Priya",  "score": 88},
    {"name": "Kiran",  "score": 65},
    {"name": "Amit",   "score": 91},
]

# Question 1 — Get all names
names = [s["name"] for s in students]
print(names)            # Q1 ["Ayush", "Rahul", "Priya","kiran", "Amit"]

# Question 2 — Get passing students (score >= 75)
passed = [s["name"] for s in students if s["score"] >= 75] 
print(passed)           # Q2 ["Ayush", Priya,"Amit"]

# Question 3 — Average score
scores = [s["score"] for s in students]
average = sum(scores) / len(scores)
print(f"Average: {average}")   # Q3 82.2

# Question 4 — Highest scorer
top = max(students, key=lambda s: s["score"])
print(f"Top: {top['name']}")   # Q4 "Ayush"

# Question 5 — Sort by score
sorted_students = sorted(students,
                         key=lambda s: s["score"],
                         reverse=True)  # ← BUG!
print(sorted_students[0]["name"])   # Q5 — who is first?