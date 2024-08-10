import pandas as pd
# this parses the batch data one symbol at a time
# it returns a dataframe with the data in the correct format

def Parse( dt_tempin ):
  # Create and load pd dataframe
  DataPar = pd.DataFrame(dt_tempin)
  # use to change name if needed


  # added 2/21/21 to fix data drops bio c etc
  #DataPar.columns = DataPar.columns.droplevel(0)  # This will remove the top header


  # Reset the index to convert the 'Date' column into a regular column
 # DataPar.reset_index(inplace=True)
  #DataPar.rename(columns={'Date': 'Index'}, inplace=True)
  # old new
#   new_column_names = {
#     'Open': 'Open',
#     'High': 'High',
#     'Low': 'Low',
#     'Close': 'Close',
#     'Volume': 'Volume'
# }

  # get importamt data
  DataPar['Open'] = DataPar['Open'].astype(float)
  DataPar['Close'] = DataPar['Close'].astype(float)
  DataPar['High'] = DataPar['High'].astype(float)
  DataPar['Low'] = DataPar['Low'].astype(float)
  DataPar['Volume'] = DataPar['Volume'].astype(float)
  # DataPar['Min'] = DataPar['Low'].min()
  SmallDataPar  = pd.DataFrame
  minx = DataPar['Low'].min()
  maxx = DataPar['High'].max()

  perx =  ((maxx-minx)/minx) * 100  # suuld be aveg   this not average
 # print(perx,minx, maxx)
  #get rid of unwanted data
  SmallDataPar = pd.DataFrame  # create empty dataframe new
  SmallDataPar  = DataPar[['Open','Close','High','Low','Volume']].copy()
  #print(SmallDataPar )
  return(SmallDataPar)