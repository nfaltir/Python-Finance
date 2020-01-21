import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style

print("\n============================Average Stock price by time frame============================\n")
timeFrame = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
stock = str(input("\nPlease enter the stock ticker:"))
stockObj = yf.Ticker(stock)
for var in timeFrame:
  stockHistory = stockObj.history(period=var)
  df = pd.DataFrame(stockHistory)
  avgPrice = sum(df['Close'])/len(df['Close'])
  print(var,"average price:",round(avgPrice,2))
  continue

minPrice = min(df['Close'])
maxPrice = max(df['Close'])

print("\nLowest Price:",round(minPrice,2))
print("Max Price:", round(maxPrice,2))