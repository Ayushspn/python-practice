import pandas as pd
df = pd.DataFrame({
    "Name":["Ayush","Ravi"],
    "Math":[85,90],
    "Science":[88,92]
})
# print(pd.melt(df, id_vars=["Name"], var_name="Subject", value_name="Score"))

df = pd.DataFrame({
    ("Math","Score"):[85,90],
    ("Science","Score"):[88,92]
}, index=["Ayush","Ravi"])
print(df.stack())
