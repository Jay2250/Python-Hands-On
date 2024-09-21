# Apple stock Data Analyse

import matplotlib.pyplot as plt
class StockData:
    df = None
    # def __init__(self,date, open, high, low, close, volume):
    #     self.name= name
    #     self.date = date
    #     self.open = open
    #     self.high = high
    #     self.low = low
    #     self.close = close
    #     self.volume= volume

    @staticmethod
    def loadData():
        try:
            StockData.df = pd.read_csv('/content/AAPL.csv')
            print(StockData.df.head())
        except Exception as e:
            print(e)

    @classmethod
    def sort_data(self):
        StockData.df.sort_values('Date')
        print(StockData.df)


s1 = StockData()
StockData.loadData()
s1.sort_data()

#-------------------------------------------------------------


plt.plot(StockData.df['Date'], StockData.df['Close'])
plt.title('Apple Stock price Analysis 1990-2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.show()
