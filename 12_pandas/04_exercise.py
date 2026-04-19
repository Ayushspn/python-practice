import pandas as pd
df = pd.DataFrame({
    "Date": ["2026-04-15", "2026-04-16", "2026-04-17"],
    "Sales": [200, 250, 300]
})

# Convert to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Set as index
df.set_index("Date", inplace=True)

print(df)