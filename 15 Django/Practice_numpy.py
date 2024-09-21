import pandas as pd
Employees = [["Jayesh",101,"CDAC",1000],["Abhishek",201,"AMDOCS",12000],["Dhanu",301,"TCS",15000]]

df1 = pd.DataFrame(Employees, columns= ['name','id','CompanyName', 'salary'])
print(df1)
# anotherDF = df[['name','id']]
df_filtered = df1[['name', 'id']]
print(df_filtered)
# print(anotherDF)