df_summary = pd.read_csv("data/01. Data-B.csv")

# Drop baris header kedua
df_summary = df_summary.iloc[1:].reset_index(drop=True)

# Rename kolom supaya clean
df_summary.columns = [
    "Stage",
    "Weight",
    "Cum_Last_Plan",
    "Cum_Last_Actual",
    "Cum_Last_Var",
    "Prog_Plan",
    "Prog_Actual",
    "Prog_Var",
    "Cum_Plan",
    "Cum_Actual",
    "Cum_Var",
    "Status"
]

# Convert numeric columns
numeric_cols = [
    "Weight",
    "Cum_Last_Plan",
    "Cum_Last_Actual",
    "Cum_Last_Var",
    "Prog_Plan",
    "Prog_Actual",
    "Prog_Var",
    "Cum_Plan",
    "Cum_Actual",
    "Cum_Var"
]

df_summary[numeric_cols] = df_summary[numeric_cols].apply(
    pd.to_numeric, errors="coerce"
)
