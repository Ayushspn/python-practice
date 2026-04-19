import pandas as pd

data = {
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai", "Lucknow", "Lucknow"],
    "Year": [2025, 2026, 2025, 2026, 2025, 2026],
    "Sales": [200, 250, 300, 350, 180, 210],
    "Profit": [50, 70, 90, 120, 40, 55]
}

df = pd.DataFrame(data)

# Pivot: average sales per city per year
pivot = pd.pivot_table(df, values="Sales", index="City", columns="Year", aggfunc="mean")
print(pivot)
