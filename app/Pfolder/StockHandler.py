# This is the main function that is called from the front end

from numpy import False_
from app.Pfolder.GetBatchData import GetBatchDataRT
from app.Pfolder.Parse import Parse
from app.Pfolder.Process2 import Process2
from app.databasehelper import save_key_value_pair
from django.shortcuts import render, redirect
import pandas as pd

# returns a dataframe with the data in the correct format and saves the data
def  handletocks(stksym,requestin):  #list of stocks , Request object, 
    #get data from yahoo
    DataAll = GetBatchDataRT(stksym)
    
    stkdata = ''   # initilize
    dfscores = pd.DataFrame(columns=['symbol', 'score','message']) # initilize
   
    # loop thru each synbol   
    for indstock in stksym:  
        # take care of the data
        Smalldf = Parse(DataAll[indstock])
        # process data
        scoreback, scoremes,Smalldf2  =  Process2(indstock, Smalldf)
        # returns score for now
        stkdata = stkdata + '<br>' + scoremes + '<br>'
       
        Smalldf2.reset_index(inplace=True)
        smalldfjson = Smalldf2.to_json(orient='records', default_handler=str)
    # save  data  symbol, score, message and smalldfjson
        save_key_value_pair(requestin,indstock,smalldfjson)   
        new_row = pd.DataFrame({'symbol' : [indstock], 'score': [scoreback],'message': [stkdata]})
        dfscores = pd.concat([dfscores, new_row], ignore_index=True)
        
    # end of loop    
    dfscores = dfscores.sort_values(by='score', ascending=False)   #sort by score
    return(dfscores, stkdata,Smalldf2 ) # done now



