# Exercise 3 — Strings
# Topic: Real world string processing
# Difficulty: ⭐⭐⭐

# Scenario: Processing user data from a form

# Question 1 — Clean user input
def clean_input(text):
    text1 = text.strip()
    return text.lower();


print(clean_input("  Ayush  "))      # "ayush"
print(clean_input("  PYTHON  "))     # "python"

# Question 2 — Validate email
def is_valid_email(email):
    if "@" not in email or email.count("@") != 1:
        return False
    return True

print(is_valid_email("ayush@gmail.com"))  # True
print(is_valid_email("ayushgmail.com"))   # False
print(is_valid_email("ayush@gmailcom"))   # False

# Question 3 — Format name
def format_name(full_name):
    test = full_name.split(" ")
    return test[::-1]

print(format_name("Ayush Sharma"))   # "Sharma, Ayush"
print(format_name("Rahul Kumar"))    # "Kumar, Rahul"

# Question 4 — Count words
def word_count(text):
    counts = {}
    for word in text.split():   # split into words
        counts[word] = counts.get(word, 0) + 1
    return counts

result = word_count("python is great python is fun")
print(result)
# {"python": 2, "is": 2, "great": 1, "fun": 1}