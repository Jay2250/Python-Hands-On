import numpy as np
import pandas as pd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
num1 = np.array([i for i in numbers[:5]])
num2 = np.array([i for i in numbers[5:10]])
num3 = np.array([i for i in numbers[10:15]])
num4 = np.array([i for i in numbers[15:]])

print(num1, num2, num3, num4)
array1 = np.append(num1, num2)
array2 = np.append(num3, num4)
print(array1, array2)

print(array1 + array2)
print(array1 * array2)
print(array1 - array2)
print(array1 ** array2)
print(np.exp(array1))


# -------------------------------------------------------------

# Time Series with Pandas
dates = pd.date_range(start='2024-01-01', periods=10, freq='D')
print(dates.dtype, dates, '\n')

# creating a time series with random data
data = np.random.randn(10)
time_series = pd.Series(data, index=dates)
print(time_series)

# access data for a specific date
print("Time series for : 2024/01/05", time_series['2024-01-05'])

# accessing data within a date range
print("Time series for range", time_series['2024-01-03':'2024-02-06'])

# boolean indexing to select dates based on a condition
print("With boolean indexing", time_series[time_series > 0])

# create a time seiers with hourly frequency
hourly_dates = pd.date_range(start='2024-01-01', periods=24, freq='H')
hourly_data = np.random.randn(24)
hourly_series = pd.Series(hourly_data, index=hourly_dates)
print("COmplete hourly series : ", hourly_series)

# accesing data for a specific dates
print(hourly_series['2024-01-01 10:00:00'])

# accessing data within a date range
print(hourly_series['2024-01-01 10:00:00':'2024-01-01 15:00:00'])

# selecting data with in a range and with a condition
print(hourly_series[(hourly_series.index >=
      '2024-01-01 10:00:00') & (hourly_series > 0)])

# accessing data for a specific date
print(time_series.loc['2024-01-05'])

# access data for a multiple specific date
print(time_series.loc['2024-01-05': '2024-02-05'])

# Access data within a date range
print(time_series.loc['2024-01-03':'2024-02-06'])

# boolean indexing to select dates based on a condition
print(time_series.loc[time_series > 0])

# accesss data for first position
print(time_series.iloc[0])

# access data for last position
print(time_series.iloc[-1])

# access data for the position from 2 to 5
print(time_series.iloc[2:5])

# Access data for a specific position
# print()

# ----------------------------------------------------------

# resampling data to a different frequency (e.g. weekly)
weekly_data = time_series.resample('W').mean()
print(weekly_data)

# calculating a 3 day moving average
rolling_mean = time_series.rolling(window=3).mean()
print(rolling_mean)

# adding a missing value
time_series['2024-01-04'] = np.nan
print(time_series)

# Forward filling missing values
filled_series = time_series.ffill()
print(filled_series)

# resample to weekly frequency
weekly_series = time_series.resample('W').mean()

# backward fill missing value
backward_filled_series = time_series.bfill()
print(backward_filled_series)

# interpolate missing values
interpolated_series = time_series.interpolate()
print(interpolated_series)

# detecting missing values
missing_values = time_series.isna()
print(missing_values)

# count missing values
missing_count = time_series.isna().sum()
print(missing_count)

# get indices of missing values
missing_indices = time_series[time_series.isna()].index[missing_values]
print(missing_indices)

# fill missing values with specific values
filled_series = time_series.fillna(0)
print(filled_series)

# drop missing values
dropped_series = time_series.dropna()
print(dropped_series)

# ----------------------------------------------------------

