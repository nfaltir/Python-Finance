import yfinance as yf
import pandas as pd


msft = yf.Ticker("MSFT")
print(msft)

#JSON data
genInfo = msft.info

historicalData = msft.history(period="max")
print(historicalData)