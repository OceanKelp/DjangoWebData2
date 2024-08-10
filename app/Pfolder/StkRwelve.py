
# This where the magic happens. This is the main file that will be run to
# process the data.  It will call the other files as needed.
  
# Using the special variable 
# __name__



from threading import main_thread
from app.Pfolder.ImportFiles import importmylib
#from app.pfolder.UserList import RunUserList
#from app/pfolder/UserList import RunUserList
#from app.Pfolder.UserList import RunUserlist

#if __name__ == "__main__":
      
   # importmylib() # import needed libraries
   # print('main')
#RunUserList() # get user list of stocks
   # exit()
#RunUserList() # get user list of stocks
   # exit())

#Run wihh user list

#from app.Pfolder.GetUserFile import GetUserList
from app.Pfolder.GetBatchData import GetBatchDataRT
from app.Pfolder.Parse import Parse
from app.Pfolder.Process2 import Process2

def RunUserList():
 ###   SYMRtnx = GetUserList()                    # get user list & user key fix data
    # pass list to get history data
    
    import pandas as pd

# Assuming 'ut' is a list
    ut = SYMRtnx

# Convert the list to a DataFrame
    df = pd.DataFrame(ut, columns=['Symbols'])

# Now 'df' is a DataFrame

    DataAll = GetBatchDataRT(df) 

    #DataAll = GetBatchDataRT(SYMRtnx)   # get the batch data back
    
    # loop thru each symbol
    for SymX in SYMRtnx:
        print('SymX2',SymX)
        Smalldf = Parse(DataAll[SymX] )   # set up small dateframe
        Process2( SymX, Smalldf)
    return(print('user list done') )



