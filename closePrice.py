
import yfinance as yf
import pandas as pd 

print("")
stock = str(input("Please enter the stock ticker:"))
stockObj = yf.Ticker(stock)


dailyPrice = stockObj.history(period="1d")

length = len(dailyPrice)

df = pd.DataFrame(dailyPrice)
closePrice = pd.DataFrame(dailyPrice, columns=["Close"])

print(closePrice)