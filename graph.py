from matplotlib import pyplot as plt
import yfinance as yf
import pandas as pd

#matplotlib theme
plt.style.use("seaborn-dark")

#enter a valid stock ticker, code breaks when you request etf(s)
stock = yf.Ticker(input("enter stock ticker: "))

#You must choose one of the following
print ("\n[1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max ]\n")

time = input("enter period: ")
priceHistory = stock.history(period=time)
stockName = stock.info['shortName']

#pandas DataFrame
df = priceHistory

#Visualize using matplotlib
plt.figure()
plt.plot(df['Close'])
plt.title(stockName + " Price history")
plt.xlabel("Time Frame: " + time)
plt.tight_layout()
plt.show()

#note, remember to exit graph window in order to re-run code. Happy Coding!
