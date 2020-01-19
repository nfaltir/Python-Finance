
import yfinance as yf
import pandas as pd 

print("\n============================Most Recent stock price============================\n")
stock = str(input("Please enter the stock ticker:"))
stockObj = yf.Ticker(stock)


dailyPrice = stockObj.history(period="1d")

length = len(dailyPrice)

df = pd.DataFrame(dailyPrice)

print(df['Close'])

