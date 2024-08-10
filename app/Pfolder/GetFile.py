# read csv file and restore to original very important
# returns a dataframe

import pandas as pd
def readcsv():
  # herb 2021-08-15
  # read and restore to original very important

  # path = r"C:\Users\herb\VS23\DjangoWebData2\DjangoWebData2"
  # df = pd.read_csv(path + '/LastRun.csv', header=[0, 1])

  path = r"C:\Users\herb\VS23\DjangoWebData2\DjangoWebData2"
  df = pd.read_csv(path + '/LastRun.csv', header=[0, 1])
  print(df,'read')
  df.drop([0], axis=0, inplace=True)  # drop this row because it only has one column with Date in it
  df[('Unnamed: 0_level_0', 'Unnamed: 0_level_1')] = pd.to_datetime(df[('Unnamed: 0_level_0', 'Unnamed: 0_level_1')], format='%Y-%m-%d')  # convert the first column to a datetime
  df.set_index(('Unnamed: 0_level_0', 'Unnamed: 0_level_1'), inplace=True)  # set the first column as the index
  df.index.name = None  # rename the index
  print(df)
  return(df)
