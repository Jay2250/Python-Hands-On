import pandas as pd
#creating a series from a list
data = [10,20,30,40,50]
series = pd.Series(data)
print(series)
#sum of all elements
print("Sum of series : ",series.sum())
#filtering values greater than 20
print("greater than 20 \n",series[series>20])
#creating a series with custom index
series = pd.Series(data, index=['a','b','c','d','e'])
print("Series with Custom index  :\n",series)
#creating a series form dictionary
data_dict = {'apple':3,'banana':2,'orange':4}
series = pd.Series(data_dict)
print("Dictionary series ", series)
#creating a series from a scalar value
series = pd.Series(10, index=['a','b','c'])        # here we can pass multiple values to a,b,c by passing a list like [10,20,30]
print("Scalar series : ",series)
#accessing element by index
print("element by index a : ",series['a'])
#slicing series
print("slicing of series : ",series['a':'c'])
#accessing element by position
print(series[1])


# -----------------------------------------------------------------
#Reading rows and columns from a csv file
dataFrame = pd.read_csv('/content/sample_data/mnist_test.csv')
print(dataFrame)

# -----------------------------------------------------------------

# Assignmnet 2 creating a dataframe with student data
data = {
    'roll no':[1,2,3,4,5],
    'name':['Alice','Bob','Charlie','David','Eve'],
    'class':[10,10,10,11,12],
    'marks':[85,45,78,97,92]
}

df = pd.DataFrame(data)
df.to_csv('student.csv', index= False)

df1 = pd.read_csv('student.csv')
print("Head of dataframe : \n",df1.head())
print("\nTail of data frame \n",df1.tail())
print("\n Info of dataframe \n",df1.info())
print("\n Describe the dataframe \n",df1.describe())

# -----------------------------------------------------------------

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 22],
    'city': ['abc', 'ABC', 'def', 'EFf', 'fasj'],
    'Score': [87, 67, 89, 92, 90]
}
df = pd.DataFrame(data)
print(df)
# selecting single column
print(df['Name'])
# multiple column
print(df[['Name', 'Score']])
# rows by inde position
print(df.iloc[0])
# selecting first 3 roe
print(df.iloc[:3])
# specific row and colunm
print(df.iloc[1:4, [0, 2]])
# row by index lab
print(df.loc[2])
# column where age > 30
print(df.loc[df['Age'] > 30])
# column where marks >80
print(df.loc[df['Score'] > 80])
# colunm where city is either from below one
print(df['city'].isin(['def', 'EFf']))


# -----------------------------------------------------------------

# Assignmnet 3 Inspection of data set
data = {
    'roll no': [1, 2, 13, 4, 5, 6, 7, 8, 9],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Abhishek', 'jayesh', 'Sammak', 'Harish'],
    'class': [10, 10, 10, 11, 12, 12, 10, 11, 12],
    'marks': [85, 45, 78, 97, 92, 87, 98, 45, 96]
}

df = pd.DataFrame(data)
df.to_csv('student1.csv', index=False)
dataf = pd.read_csv('student1.csv')
print("First 5 row : ", dataf.head())
print("Specific colunms : ", dataf[['name', 'marks']])
print(dataf.loc[(dataf['class'] == 10) & (dataf['marks'] > 75)])
print("First 5 rows and 3 columns :\n ", dataf.iloc[0:5, [1, 2, 3]])
print("rows from 5 to 9 and column are name marks: ",
      dataf.loc[4:8, ['name', 'marks']])


# --------------------------------------------------------------------

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
        }
df = pd.DataFrame(data)
print(df)
# adding a new column Score with default value
df['Score'] = [90, 87, 98, 56]
print("dataframe after adding values\n", df)
# Deleting the city column
df = df.drop('City', axis=1)
print("Dataframe after deleteing City column \n", df)
# sorting by age in ascending order
sorted_By_age = df.sort_values(by='Age')
print('\nDataframe sorted by age\n', sorted_By_age)
# renaming  score col to final score col
df = df.rename(columns={'Score': 'Final Score'})
print('\n DataFrame after renamingg \n', df)
# creating a dataframe with missing value
data_with_nan = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, None, 35, None],
    'Score': [86, 90, None, 78]
}
df_nan = pd.DataFrame(data_with_nan)
# filing missing value in age with mean age
df_nan['Age'] = df_nan['Age'].fillna(df_nan['Age'].mean())
print('\n Dataframe after filling missing values in Age with mean age \n', df_nan)
# filling missing value in 'Score' with fixed value (e.g 0)
df_nan['Score'] = df_nan['Score'].fillna(0)
print('\n Dataframe after filling missing values in Score with 0 \n', df_nan)
# droping rows with any missing value
print("original ", df_nan)
df_dropped = df_nan.dropna()
print('\n Dataframe after dropping rows with missing values \n', df_dropped)
# replacing specific values in the 'name' column
df_nan['Name'] = df_nan['Name'].replace({'Alice': 'John'})
print('\n Dataframe after replacing Alice with John \n', df_nan)

