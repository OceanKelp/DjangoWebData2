import pandas as pd
# read csv file and restore to original very important
# returns a dataframe
def readcsv():
  # herb 2021-08-15
  # read and restore to original very important
  #pd.read_csv('LastRun.csv', index_col=0) try this


  path = r"C:\Users\herb\VS23\DjangoWebData2\DjangoWebData2"
  df = pd.read_csv(path + '/LastRun.csv', header=[0, 1])

  #df = pd.read_csv('LastRun.csv', header=[0, 1])
  df.drop([0], axis=0, inplace=True)  # drop this row because it only has one column with Date in it
  df[('Unnamed: 0_level_0', 'Unnamed: 0_level_1')] = pd.to_datetime(df[('Unnamed: 0_level_0', 'Unnamed: 0_level_1')], format='%Y-%m-%d')  # convert the first column to a datetime
  df.set_index(('Unnamed: 0_level_0', 'Unnamed: 0_level_1'), inplace=True)  # set the first column as the index
  df.index.name = None  # rename the index
  return(df)
