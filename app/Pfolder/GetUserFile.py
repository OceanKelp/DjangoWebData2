# get file from user driv#e and returns a sring of symbols
import pandas as pd

def GetFileUpload(filein):
    dfr = pd.read_csv('C:/Users/herb/VS23/DjangoWebData2/app.uploads/' + filein + '.csv')
    dfx = dfr['Symbol'].tolist()
    return(dfx)


