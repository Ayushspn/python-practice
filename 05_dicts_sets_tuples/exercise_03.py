# Exercise 3 — Dicts, Sets, Tuples
# Topic: Real world data processing
# Difficulty: ⭐⭐⭐

# Scenario: E-commerce order system

orders = [
    {"id": 1, "customer": "Ayush",  "items": ["laptop", "mouse"]},
    {"id": 2, "customer": "Rahul",  "items": ["keyboard", "mouse"]},
    {"id": 3, "customer": "Priya",  "items": ["laptop", "webcam"]},
    {"id": 4, "customer": "Ayush",  "items": ["headphones"]},
]

# Question 1 — Count orders per customer
# Expected: {"Ayush": 2, "Rahul": 1, "Priya": 1}
customer_orders = {}
for order in orders:
    name = order["customer"]
    customer_orders[name] = customer_orders.get(name, 0) + 1
print(customer_orders)   # Q1  {"Ayush": 2, "Rahul": 1, "Priya": 1}

# Question 2 — Get unique items sold
# Expected: {"laptop","mouse","keyboard","webcam","headphones"}
all_items = []
for order in orders:
    all_items.extend(order["items"])
unique_items = set(all_items)
print(unique_items)      # Q2 {"laptop","mouse","keyboard","webcam","headphones"}

# Question 3 — Find customers who ordered laptop
laptop_customers = [o["customer"] for o in orders
                    if "laptop" in o["items"]]
print(laptop_customers)  # Q3 ["Ayush", "Priya"]

# Question 4 — Most ordered item
item_counts = {}
for order in orders:
    for item in order["items"]:
        item_counts[item] = item_counts.get(item, 0) + 1
most_ordered = max(item_counts, key=item_counts.get)
print(most_ordered)      # Q4 — which item? laptop

# Question 5 — Fix this bug!
def get_customer_items(orders):
    result = {}
    for order in orders:
        name  = order["customer"]
        items = order["items"]
        if name in result:
            result[name] = result[name] + items  # BUG?
        else:
            result[name] = items                 # BUG?
    return result

customer_items = get_customer_items(orders)
print(customer_items["Ayush"])   # Q5 — what prints?
# Expected: ["laptop","mouse","headphones"]
# Is there a bug?