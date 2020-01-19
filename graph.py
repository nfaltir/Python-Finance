
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
import datetime as dt


print("\n=========================Stock Price Grapher=========================\n")
stock = str(input("Please enter the stock ticker:"))

stockObj = yf.Ticker(stock)



y = "\n[***** 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max============*****]\n"

print(y)
time = input("Please enter time frame?:")
timeFrame = stockObj.history(period=time)

length = len(timeFrame)

df = pd.DataFrame(timeFrame)
plt.style.use('bmh')
plt.ylabel('Price ($USD)',fontsize=15)
plt.xlabel('Date',fontsize=15)

df['Close'].plot(figsize=(12,6))




plt.title("Price History", fontsize=25)
plt.show()
