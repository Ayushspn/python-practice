import pandas as pd

# s = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print(s)


data = {
    "Name": ["Ayush", "Ravi", "Neha"],
    "Age": [24, 30, 22],
    "City": ["Delhi", "Mumbai", "Lucknow"]
}
df = pd.DataFrame(data)
#print(df)

print(df.head(1))
print(df.info())
