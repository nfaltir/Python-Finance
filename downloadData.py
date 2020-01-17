
import yfinance as yf
import pandas as pd 


print("\n============================Download Stock Data============================\n")

stock = str(input("Please enter the stock ticker:"))
stockObj = yf.Ticker(stock)
hist_price_Data = stockObj.history(period="max")
df = pd.DataFrame(hist_price_Data)


fileName = str(input("please enter csv file name:") + ".csv")


#reads new data as csv file
csvData = df.to_csv(r'%s'%fileName)
print("\ndownload complete!")



