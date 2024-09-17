import pandas as pd

data = pd.read_csv(r'/content/WCHN.csv')

data.set_index('Date', inplace=True)
print(data.head())

data.isna()

split_index = int(0.8*len(data))
train_data = data.iloc[:split_index]
test_data = data.iloc[split_index:]

print(train_data)
print(test_data)
window_size = 3
forecast = train_data.rolling(window=window_size).mean().iloc[-len(test_data):]

print(forecast)

comparision = pd.DataFrame(
    {'Actual': test_data['Close'], 'Forecast': forecast['Close']})
print(comparision)

# Calculate the mean absolute error as a simple evaluation
mae = np.mean(np.abs(comparision['Actual']-comparision['Forecast']))
print(mae)

# ---------------------------------------------------------------

