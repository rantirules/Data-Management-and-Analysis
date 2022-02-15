import pandas as pd

data = pd.read_csv('covid.csv')
subset = data[["date", "new_cases"]]
print(subset.groupby("date").mean()[:14])
