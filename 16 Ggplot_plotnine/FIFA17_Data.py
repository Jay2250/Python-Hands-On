import pandas as pd
from plotnine import ggplot, aes, geom_point, labs, geom_line, geom_bar
# Assuming you have the fifa17 dataset in a CSV file named 'fifa17.csv'
# Replace 'fifa17.csv' with the actual file name if it's different.

fifa_df = pd.read_csv(r'/content/FIFA17_official_data.csv')

# Display the first few rows of the DataFrame
print(fifa_df.head())

# selecting columns Name and Best Overall Rating
new_df = fifa_df[['Name', 'Best Overall Rating']]
print(new_df)
new_df.dropna()
new_df['Name'] = new_df['Name'].drop_duplicates()
new_df

# sorting new unique player by overall rating in descending order
new_df.sort_values(by='Best Overall Rating', ascending=False)
df = new_df.head()
df
# creating a bar plot
bar_plot = (ggplot(df, aes(x='Name', fill="Best Overall Rating")) +
            geom_bar()+labs(title='Bar Plot Example', x='X Axis', y='Y Axis'))
print(bar_plot)
