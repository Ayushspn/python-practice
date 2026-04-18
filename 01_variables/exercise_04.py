# Exercise 4 — Variables & References
# Topic: Putting it all together
# Difficulty: ⭐⭐⭐⭐

# Scenario: You're building a student grade tracker

# Question 1 — What prints?
grades = {"Ayush": [90, 85, 92]}
backup = grades
backup["Rahul"] = [70, 75, 80]

print(len(grades))    # Q1: 1 or 2? 2

# Question 2 — What prints?
grades = {"Ayush": [90, 85, 92]}
backup = grades.copy()
backup["Rahul"] = [70, 75, 80] 

print(len(grades))    # Q2: 1 or 2? 2

# Question 3 — Tricky! What prints?
grades = {"Ayush": [90, 85, 92]}
backup = grades.copy()
backup["Ayush"].append(95)    # modifying LIST inside dict!

print(grades["Ayush"])  # Q3: [90,85,92] or [90,85,92,95]? [90,85,92,95]

# Question 4 — Fix Q3 using deepcopy
import copy
grades = {"Ayush": [90, 85, 92]}
backup = copy.deepcopy(grades)
backup["Ayush"].append(95)

print(grades["Ayush"])  # Q4: [90,85,92] or [90,85,92,95]? [90,85,92]

# Question 5 — Real world function
# Fix this function so each student gets their OWN grade list!
def add_student(name, initial_grades={}):
    initial_grades[name] = []
    return initial_grades

s1 = add_student("Ayush")
s2 = add_student("Rahul")

print(len(s1))   # Q5a: 1 or 2?
print(len(s2))   # Q5b: 1 or 2?

# Write the fix below ↓
def add_student_fixed(name, initial_grades=None):
    # YOUR CODE HERE
    pass