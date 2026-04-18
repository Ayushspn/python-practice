# Exercise 3 — Data Types
# Topic: Real world data validation
# Difficulty: ⭐⭐⭐

# Scenario: You're validating user input for a form

# Question 1 — Fix this validation function
def validate_age(age):
    if age:           # BUG! what if age = 0?
        return True
    return False

print(validate_age(25))   # Q1a: should be True True
print(validate_age(0))    # Q1b: should be True (0 is valid age!) FALSE
print(validate_age(None)) # Q1c: should be False FALSE

# Fix below ↓
def validate_age_fixed(age):
    if age is None:
     return False
    return True

# Question 2 — What prints?
user_input = "  "     # user entered just spaces!
if user_input:
    print("Valid input!")     # Q2a: prints or not? Empty input!
else:
    print("Empty input!")

# Better validation:
if user_input.strip():
    print("Valid input!")
else:
    print("Empty input!")    # Q2b: prints or not?

# Question 3 — Type checking
def process_score(score):
    if not isinstance(score, (int, float)):
        raise TypeError(f"Expected number, got {type(score).__name__}")
    if score < 0 or score > 100:
        raise ValueError(f"Score must be 0-100, got {score}")
    return score

try:
    process_score("95")   # Q3a: works or error?
except TypeError as e:
    print(f"TypeError: {e}")

try:
    process_score(150)    # Q3b: works or error?
except ValueError as e:
    print(f"ValueError: {e}")

print(process_score(95))  # Q3c: what prints?