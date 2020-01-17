
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
import datetime as dt


print("")
stock = str(input("Please enter the stock ticker:"))
stockObj = yf.Ticker(stock)


dailyPrice = stockObj.history(period="max")

length = len(dailyPrice)

df = pd.DataFrame(dailyPrice)
plt.style.use('bmh')
plt.ylabel('Price ($USD)',fontsize=15)
plt.xlabel('Date',fontsize=15)

df['Close'].plot(figsize=(12,6))




plt.title("Price History", fontsize=25)
plt.show()
