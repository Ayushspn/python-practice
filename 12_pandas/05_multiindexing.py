import pandas as pd

data = {
    ("Math", "Score"): [85, 90, 78],
    ("Science", "Score"): [88, 92, 80],
    ("Science", "Grade"): ["B", "A", "C"]
}

df = pd.DataFrame(data, index=["Ayush", "Ravi", "Neha"])
# print(df)


df1 = pd.DataFrame({
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai"],
    "Year": [2025, 2026, 2025, 2026],
    "Sales": [200, 250, 300, 350]
})

df1 = df1.set_index(["City", "Year"])
print(df1)

print(df1.loc[("Delhi", 2026)])