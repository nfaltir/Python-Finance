
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
import datetime as dt


print("\n======================= Stock Price by time frame =========================\n")

stock = str(input("Please enter the stock ticker:"))
stockObj = yf.Ticker(stock)

y = "\n[***** 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max============*****]\n"
print(y)

time = input("Please enter time frame?:")
timeFrame = stockObj.history(period=time)

df = pd.DataFrame(timeFrame)
avgPrice = sum(df['Close'])/len(df['Close'])

print("\nThe",time,"average price is:",round(avgPrice,2))