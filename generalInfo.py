import yfinance as yf
import pandas as pd


# user stock ticker input
sTicker = str(input("Please enter stock ticker:"))

# Retruns UPPER case ticker symbol
stock = sTicker.upper()
stockObj = yf.Ticker(stock)
# General Data
genData = stockObj.info
#df = pd.DataFrame(genData)

for metrics in genData.items(): 
    metrics = (str(metrics).replace("(","").replace(")", "").replace(",",":").replace("'",""))
    print(metrics)












