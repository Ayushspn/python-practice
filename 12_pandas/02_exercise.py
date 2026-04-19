import pandas as pd

df = pd.DataFrame({
    "Name": ["Ayush", "Ravi", "Neha"],
    "Age": [24, 30, 22],
    "City": ["Delhi", "Mumbai", "Delhi"]
})

# print(df)

# Select column
# print(df["Name"])

# # Select row by label
# print(df.loc[0])

# # Select row by position
# print(df.iloc[1])

# # Boolean filtering
# print(df[df["City"] == "Delhi"], 'df[df["City"] == "Delhi"]')


# Average age per city
print(df.groupby("City")["Age"].mean())

# Youngest person in each city
print(df.groupby("City")["Age"].min())

