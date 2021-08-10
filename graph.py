from matplotlib import pyplot as plt
import yfinance as yf
import pandas as pd

plt.style.use("seaborn-dark")

stock = yf.Ticker(input("enter stock ticker: "))
print ("\n[1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max ]\n")
time = input("enter period: ")
priceHistory = stock.history(period=time)
stockName = stock.info['shortName']

#pandas DataFrame
df = priceHistory

plt.figure()
plt.plot(df['Close'])
plt.title(stockName+ " Price history")
plt.xlabel("time frame: " + time)
plt.tight_layout()
plt.show()
