import pandas as pd
df_scores = pd.DataFrame({"ID":['a','b',3], "Score":[90,85,88]})
df_names = pd.DataFrame({"ID":[1,2,3], "Name":["Ayush","Ravi","Neha"]})

merged = pd.merge(df_names, df_scores, on="ID")
print(merged)