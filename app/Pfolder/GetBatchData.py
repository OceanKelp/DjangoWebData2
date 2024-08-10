
from datetime import timedelta
from datetime import date
from datetime import datetime, timedelta, date
import pytz  #  time zone
import yfinance  as yf
from yfinance import download
import pandas as pd
#changed to use list
def GetBatchDataRT(symlist):
 # need this  list input for yf.download
  #ticker_list = ['C','AAPL','ABT','ADSK','AI','ALB']
 # tickers = symlist['Symbols'].tolist()  
  tickers = symlist
  # todaya date and 210 days  ago
  new_york = pytz.timezone('America/New_York')
  ny_time = datetime.now(new_york)
  end_date =ny_time
 # end_date = date.today()
  start_date = end_date - timedelta(days=365)
  # Here we use yf.download function
  #Make sure to provide the dates in the "YYYY-MM-DD" format. For example, "2023-01-01" for January 1, 2023.
  data = yf.download(tickers,  threads=True, start=start_date, end=end_date, group_by='ticker',)
 # data = yf.download(tickers,  threads=True, start=start_date, end=end_date, group_by='ticker',)
  df = pd.DataFrame
  df =data
 
# Export the DataFrame to a CSV file without repeating column names
  # not used
 
  return(df)
