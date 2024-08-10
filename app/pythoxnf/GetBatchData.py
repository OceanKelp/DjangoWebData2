
from datetime import timedelta
from datetime import date
import yfinance  as yf
from yfinance import download
import pandas as pd

def GetBatchDataRT(symlist):
 # need this  list input
  #ticker_list = ['C','AAPL','ABT','ADSK','AI','ALB']
  tickers = symlist['Symbol'].tolist()  
  
  # todaya date and 210 days  ago
  end_date = date.today()
  start_date = end_date - timedelta(days=365)
  # Here we use yf.download function
  #Make sure to provide the dates in the "YYYY-MM-DD" format. For example, "2023-01-01" for January 1, 2023.
  data = yf.download(tickers,  threads=True, start=start_date, end=end_date, group_by='ticker',)
  df = pd.DataFrame
  df =data
  print(data)
  path = r"C:\Users\herb\VS23\DjangoWebData2\DjangoWebData2"
  df.to_csv(path + '/LastRun.csv', index=True)   # index true means save the index column
  return(data)
 
