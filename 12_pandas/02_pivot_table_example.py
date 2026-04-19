# import pandas as pd
# sales = pd.DataFrame({
#     "Customer": ["A","A","B","B","C","C"],
#     "Product": ["Laptop","Phone","Laptop","Tablet","Phone","Tablet"],
#     "Amount": [1200, 800, 1300, 600, 700, 500]
# })

# pivot = pd.pivot_table(sales, values="Amount", index="Customer", columns="Product", aggfunc="sum", fill_value=0)
# print(pivot)


import pandas as pd

df = pd.DataFrame({
    "Name": ["Ayush", "Ravi", "Neha"],
    "Age": [24, None, 22],
    "City": ["Delhi", "Mumbai", None]
})

# Drop rows with missing values
# df_clean = df.dropna()

#print(df_clean)

# Fill missing ages with mean
# df["Age"].fillna(df["Age"].mean(), inplace=True)


# # Fill missing city with placeholder
# df["City"].fillna("Unknown", inplace=True)
# print(df)


df1 = pd.DataFrame({
    "City": ["Delhi", "Mumbai", "Lucknow"],
    "Sales": [200, 300, 180]
})

# One-hot encoding
df_encoded = pd.get_dummies(df1, columns=["City"], drop_first=True)
print(df_encoded)

