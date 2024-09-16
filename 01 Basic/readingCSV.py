import pandas as pd
df1 = pd.read_csv("C:\\Users\\DAI.STUDENTSDC\\Desktop\\Document.csv")
print("Head of dataframe : \n",df1.head(2))
print("\nTail of data frame \n",df1.tail(5))
print("---------Info--Of--DataFrame-------------")
print(df1.info())
print("\n Describe the dataframe \n",df1.describe())