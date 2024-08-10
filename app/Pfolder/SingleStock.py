# Run a single stock old or new data
#def OneSymbolNewData(SymbolIn):
#DOES NOT WORK
from Finish import finish
from GetBatchData import GetBatchData


Symboluser = input("Enter Stock Symbol  ")
SymboluserU = Symboluser.upper()
# 2 Check if last run data is loaded.  Then use that data else  load data or look up new data
#Run with old data
if(1==1):  #  OS.path.exists('/content/LastRun.csv'):
   dfo = pd.read_csv('LastRun.csv')
      #dfo = pd.read_fwf('LasrRun.csv')
   sym = pd.read_csv('YourSymbols.csv')
   sym.values.tolist()
   s = SymboluserU
   if(s in sym):
      print('here')
   else:
      print('not here')
   print(dfo, SymboluserU)
   print('file not found')
   try:# see if th at symbol is in old data
      #dfo = pd.readcsv()
      dfo = pd.read_csv('LastRun.csv')
      #dfo = pd.read_fwf('LasrRun.csv')
      print(dfo, SymboluserU)
      dfox = dfo[SymboluserU ]

      print('RAN WITH OLD DATA')
      finish(SymboluserU, dfox)
   except:  # get new data
      dfox = GetBatchData([SymboluserU])
      finish(SymboluserU, dfox)
      print('Ran with new data')
else:
  dfox = GetBatchData([SymboluserU]) #no old data
  finish(SymboluserU, dfox)
  print('Ran with new data')


