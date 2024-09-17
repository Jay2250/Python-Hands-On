# quartile
import pandas as pd
data = {'Values': [10, 12, 12, 13, 12, 14, 10, 13, 13, 400]}
df = pd.DataFrame(data)

# calculating Q1 Q3 and IQR
Q1 = df['Values'].quantile(0.25)
print(Q1)
Q3 = df['Values'].quantile(0.75)
print(Q3)
IQR = Q3-Q1
print(IQR)

# define bound for outliners
lower_bound = Q1-1.5*IQR
print(lower_bound)
upper_bound = Q3 + 1.5*IQR
print(upper_bound)

# identity outliners
outliners = df[(df['Values'] < lower_bound) | (df['Values'] > upper_bound)]
print("ouliners: \n ", outliners)

