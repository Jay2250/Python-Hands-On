import matplotlib.pyplot as plt
import numpy as np

# sample data
x1 = np.arange(1, 11)
y1 = [1, 3, 4, 7, 9, 12, 15, 18, 19, 22]
y2 = [2, 5, 7, 10, 12, 13, 16, 18, 21, 23]

# 1. line plot
plt.figure(figsize=(16, 8))
plt.plot(x1, y1, label='Dataset 1', color='blue', marker='o', linestyle='--')
plt.plot(x1, y2, label='Dataset 2', color='red', marker='*', linestyle='-')
plt.title('Line Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()

# bar chart
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [10, 15, 20, 12]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='purple')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000*np.random.rand(50)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# sub plot
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

axs[0, 0].plot(x1, y1, label='Dataset 1', color='blue',
               marker='o', linestyle='--')
axs[0, 0].plot(x1, y2, label='Dataset 2',
               color='red', marker='*', linestyle='-')
axs[0, 0].set_title('Line Plot Example')
axs[0, 0].set_xlabel('X-axis')
axs[0, 0].set_ylabel('Y-axis')
axs[0, 0].legend()
axs[0, 0].grid(True)

axs[0, 1].bar(categories, values, color='purple')
axs[0, 1].set_title('Bar Chart Example')
axs[0, 1].set_xlabel('Categories')
axs[0, 1].set_ylabel('Values')


axs[1, 0].scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
axs[1, 0].set_title('Scatter Plot Example')
axs[1, 0].set_xlabel('X-axis')
axs[1, 0].set_ylabel('Y-axis')


axs[1, 1].pie(values, labels=categories, autopct='%1.1f%%')
axs[1, 1].set_title('Pie Chart Example')
plt.show()


# --------------------------------------------------------------------

# Assignment 1 : ploting sales data for a year. Using matplotlib for creating line plots and bar charts and pie charts
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales_data = np.random.randint(100, 500, size=(12, 5))
print(sales_data)
plt.figure(figsize=(20, 8))
plt.plot(months, sales_data, label=products)
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

dataA = sales_data[:, 0]
dataB = sales_data[:, 1]
dataC = sales_data[:, 2]
dataD = sales_data[:, 3]
dataE = sales_data[:, 4]


print('------------Bar Chart-------------')
plt.figure(figsize=(6, 4))
plt.bar(months, dataA, width=0.8, label=products[0])
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()


plt.bar(months, dataB, width=0.8, label=products[1])
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()

plt.figure(figsize=(16, 8))
plt.bar(months, dataC, width=0.8, label=products[2])
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()

plt.figure(figsize=(16, 8))
plt.bar(months, dataD, width=0.8, label=products[3])
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()

plt.figure(figsize=(16, 8))
plt.bar(months, dataE, width=0.8, label=products[4])
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()
# plt.bar(months,dataD, width=0.8, label=products[3])
# plt.bar(months,dataE, width=0.8, label=products[4])

# -------------------------------------------------------------------

print("-----------Pie Chart---------------")
for i in range(12):
    plt.figure(figsize=(16, 8))
    plt.pie(sales_data[i], labels=products, autopct='%1.2f%%')
    plt.title(f'Sales Data for  {months[i]}')
plt.show()


# --------------------------------------------------------------------

