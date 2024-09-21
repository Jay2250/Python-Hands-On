#gg plot  - Grammar of graphics
# part of plotnine library

# graphs offered
from plotnine import ggplot, aes, geom_bar, labs
   #   line
   #   bar
   #   scatter
   #   violin
   #   Area
   #   Heatmap, etc

#-----------------------------------------------------------

import pandas as pd
from plotnine import ggplot, aes, geom_point, labs, geom_line, geom_bar


data = pd.DataFrame({

    'x': pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    'y': pd.Series([2, 4, 5, 7, 11, 13, 17, 19, 23, 29]),
    'category': pd.Series(['A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B'])

})

scatter_plot = (ggplot(data, aes(x='x', y='y', color='category')) +
                geom_point()+labs(title='Scatter Plot Example', x='X Axis', y='Y Axis'))
print(scatter_plot)


line_plot = (ggplot(data, aes(x='x', y='y', color='category')) +
             geom_line()+labs(title='Line Plot Example', x='X Axis', y='Y Axis'))
print(line_plot)

bar_plot = (ggplot(data, aes(x='x', fill="category", color='category')) +
            geom_bar()+labs(title='Bar Plot Example', x='X Axis', y='Y Axis'))
print(bar_plot)


# ----------------------------------------------------------


# Sample data
data = pd.DataFrame({
    'Name': ['A', 'B', 'A', 'C', 'B', 'C', 'A'],
    'Best Overall Rating': ['Good', 'Average', 'Good', 'Excellent', 'Average', 'Good', 'Excellent']
})

# Create a bar plot
bar_plot = (ggplot(data, aes(x='Name', fill='Best Overall Rating')) +
            geom_bar() +
            labs(title='Bar Plot Example', x='Name', y='Count'))

print(bar_plot)
