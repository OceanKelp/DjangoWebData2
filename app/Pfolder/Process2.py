# calculate technical idicators to plot
# plot stock data
from app.Pfolder.Message import StatusMessage
import pandas as pd
from app.databasehelper import save_key_value_pair
global ages


def Process2(symbolin, dt_Pan):
   
      # setup
      Symbol = symbolin
      Per = .02   # bol per for uo & low band

    # calculate technical idicators to plot
      dt_Pan['MA20'] = dt_Pan['Close'].rolling(window=20).mean()
      dt_Pan['MA50'] = dt_Pan['Close'].rolling(window=50).mean()
      dt_Pan['20dSTD'] = dt_Pan['Close'].rolling(window=20).std()
      dt_Pan['UpperBol'] =  dt_Pan['MA20'] + ( dt_Pan['20dSTD'] * 2)
      dt_Pan['LowerBol'] = dt_Pan['MA20'] - (dt_Pan['20dSTD'] * 2)
      dt_Pan['UpperminusPer'] =  dt_Pan['UpperBol'] -  dt_Pan['UpperBol'] * Per
      dt_Pan['lowerPlusPer'] =  dt_Pan['LowerBol']  + ( dt_Pan['LowerBol'] * Per )
      dt_Pan['difBol'] = dt_Pan['UpperBol'] - dt_Pan['LowerBol']

     # get message & score
      pointsgood = pointsbad = 0
      messagegood, messagebad,  pointsgood, pointsbad =  StatusMessage(dt_Pan , Symbol)
      score = pointsgood -pointsbad
    
      # make indicator tests
      ages = Symbol +  '  Score = %d  '  %score + messagegood +  'pointsgood = %d  ' %pointsgood +   messagebad + ' Bad = %d  '  %pointsbad

      # calculate money flow
      # not what this is fro MFResult = pd.DataFrame()
  
      # intiulize shortdf
      #shortdf = pd.DataFrame()
  
      Days = 50
      length = len(dt_Pan)
      Dayreferance = length - Days # get lenhth to end
      shortdf2 = dt_Pan[Dayreferance : length]
      return(score, ages, shortdf2)  # herb fix this
 






  #print(Symbol,'  Score  ', score, '  ', ages)
  # if score > -70: #10:
  #   Days = 50
  #   length = len(dt_Pan)
  #   Dayreferance = length - Days # get lenhth to end
  #   shortdf = dt_Pan[Dayreferance : length]
    
   # print(' shortdf' ,shortdf)
    # HerbFlow(Symbol, shortdf )
    
    #plot(shortdf, Symbol, messages)  herb plot
    #plot(shortdf, Symbol)
   #return(shortdf) 
