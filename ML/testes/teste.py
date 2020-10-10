import pandas as pd

dataset = pd.read_csv("Salary_Data.csv")

mat_Feat = dataset.iloc[:, :-1 ].values

mat_Feat2 = dataset.iloc[:, :-1 ]

print(mat_Feat)
print()
print(mat_Feat2)