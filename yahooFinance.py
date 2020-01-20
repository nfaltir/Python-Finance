import yfinance as yf
import pandas as pd


# user stock ticker input
sTicker = str(input("Please enter stock ticker:"))

# Retruns UPPER case ticker symbol
stock = sTicker.upper()
stockObj = yf.Ticker(stock)


# General Data
genData = stockObj.info

# Historical Data
histData = stockObj.history(period="max")

# get Dividend Data
dividend = stockObj.dividends

# get stock historical splits
stockSplits = stockObj.splits

# get dividend plus splits (actions)
sActions = stockObj.actions










# output
# print(genData)
#print(histData)
#print(dividend)
#print(stockSplits)
#print(sActions)

stop = input("")
