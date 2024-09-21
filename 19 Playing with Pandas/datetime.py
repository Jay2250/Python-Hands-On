# prompt: create a csv file with columns unitid, temp, datetime example  : 1,38,2024-09-21T15:30:00

import pandas as pd
import re
import csv
import datetime

# Sample data
data = [
    {'unitid': 1, 'temp': 38, 'datetime': '2024-09-21T15:30:00'},
    {'unitid': 2, 'temp': 35, 'datetime': '2024-09-21T16:00:00'},
    {'unitid': 3, 'temp': 39, 'datetime': '2024-09-21T16:30:00'},
]

# Specify the CSV file name
csv_file_name = 'temperature_data.csv'

# Write the data to the CSV file
with open(csv_file_name, 'w', newline='') as csvfile:
    fieldnames = ['unitid', 'temp', 'datetime']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

print(f"CSV file '{csv_file_name}' created successfully.")


df = pd.read_csv('temperature_data.csv')
df['datetime'] = pd.to_datetime(df['datetime'])
df['date'] = df['datetime'].dt.date
df['time'] = df['datetime'].dt.time
print(df)

date_pattern = r'\d{4}-\d{2}-\d{2}'
time_pattern = r'\d{2}:\d{2}:\d{2}'

df['date1'] = df['date'].apply(lambda x: re.search(
    date_pattern, str(x)).group() if re.search(date_pattern, str(x)) else None)
df['time1'] = df['time'].apply(lambda x: re.search(
    time_pattern, str(x)).group() if re.search(time_pattern, str(x)) else None)

print(df)

df.to_csv('temperature_data_new.csv', index=False)
