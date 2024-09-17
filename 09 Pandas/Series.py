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


# ----------------------------------------------------------------

# creating a series
data = pd.Series([10, 20, 20, 20, 30, 40, 40])
# ranking with different methods
print("Average rank :")
print(data.rank(method='average'))
print("\nMin Rank")
print(data.rank(method='min'))
print("\n Max Rank")
print(data.rank(method='max'))
print("\n First Rank : ")
print(data.rank(method='first'))
print("\n last rank ")
print(data.rank(method='dense'))


