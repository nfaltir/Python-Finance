
import yfinance as yf
import pandas as pd 


print("\n============================Download Stock Data============================\n")

stock = str(input("Please enter the stock ticker:"))
stockObj = yf.Ticker(stock)

y = "\n[***** 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max============*****]\n"

print(y)
time = input("Please enter time frame?:")

hist_price_Data = stockObj.history(period=time)
df = pd.DataFrame(hist_price_Data)


fileName = str(input("please enter csv file name:") + ".csv")


#reads new data as csv file
csvData = df.to_csv(r'%s'%fileName)
print("\ndownload complete!")



