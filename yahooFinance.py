import yfinance as yf
import pandas as pd


#user stock ticker input
sTicker = str(input("Please enter stock ticker:"))

#Retruns UPPER case ticker symbol
stock = sTicker.upper()
print("\nStock ticker:", stock)


stockObj = yf.Ticker(stock)
print(stockObj)

#General Data
genData = stockObj.info

#Historical Data

histData = stockObj.history(period="max")

print(genData)
print(histData)




