import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = sns.load_dataset('iris')
print(df.head())

# ---------------------------------------------------------------

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='species', style='species', palette='Set2', s=100)
plt.title('Scatter Plot of Iris Dataset : Petal Length vs Petal Width')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()

# ---------------------------------------------------------------

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='species', y='sepal_length')
plt.title('Box Plot of Iris Dataset : Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length')
# plt.show()

# ---------------------------------------------------------------

plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='sepal_width', hue='species', kde=True)
plt.title('Histogram of Iris Dataset : Sepal Width by Species')
plt.xlabel('Sepal Width')
plt.ylabel('Frequency')
plt.show()

# ---------------------------------------------------------------

plt.figure(figsize=(8, 6))
sns.violinplot(data=df, x='species', y='petal_length')
plt.title('Violin Plot of Iris Dataset : Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length')
plt.show()

# ---------------------------------------------------------------

plt.figure(figsize=(8, 6))
sns.pairplot(data=df, hue='species', palette='Set2')
plt.suptitle('Pair Plot of Iris Dataset', y=1.02)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# ---------------------------------------------------------------

# Assignment 2 same data with seaborn

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales_data = np.random.randint(100, 500, size=(12, 5))
# print(sales_data)
df = pd.DataFrame(sales_data, columns=products, index=months)
print(df)
plt.figure(figsize=(20, 8))
sns.lineplot(data=df)
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 8))
sns.barplot(data=df, )
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
# plt.show()

plt.figure(figsize=(8, 8))
sns.violinplot(data=df)
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()

# ---------------------------------------------------------------

