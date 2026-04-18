# Exercise 3 — Variables & References
# Topic: Real world bugs
# Difficulty: ⭐⭐⭐

# Scenario: You're building a shopping cart system

# Bug 1 — Find the bug and fix it!
def create_cart(items=[]):
    return items

cart1 = create_cart()
cart1.append("apple")

cart2 = create_cart()
cart2.append("banana")

print(cart1)   # Q1: expected ["apple"] but what actually prints? [apple]
print(cart2)   # Q2: expected ["banana"] but what actually prints? [apple, banana]

# Fix the bug below ↓
def create_cart_fixed(items=None):
    # YOUR FIX HERE
    if items is None:
        items = []
    return items

# Bug 2 — Find the bug!
user1 = {"name": "Ayush", "cart": []}
user2 = user1          # trying to create new user

user2["name"] = "Rahul"
user2["cart"].append("laptop")

print(user1["name"])   # Q3: "Ayush" or "Rahul"? Rahul 
print(user1["cart"])   # Q4: [] or ["laptop"]? ["laptop"]

# Fix below ↓
import copy
user1 = {"name": "Ayush", "cart": []}
user2 = copy.deepcopy(user1)   # YOUR FIX

user2["name"] = "Rahul"
user2["cart"].append("laptop")

print(user1["name"])   # Q5: "Ayush" or "Rahul"? "Ayush"
print(user1["cart"])   # Q6: [] or ["laptop"]? []