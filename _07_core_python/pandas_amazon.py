import matplotlib
import pandas as pd
import mplfinance as mpl

file = "AMZN.csv"
data = pd.read_csv(file)
print(data)
data.Date =pd.to_datetime(data.Date)
data.info()
data = data.set_index("Date")
print(data)
mpl.plot(data,type='candle',figratio=(20,12),title='Amazon price 2019/2020',volume=True,tight_layout=True,style='yahoo')