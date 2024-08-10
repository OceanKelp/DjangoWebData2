 #Create Bollingerbands
def Bollinger(StockData, symin):
   # setup
    howmany = 1    # this determines how many of the end of the list are tested
    length = len(StockData)
    lfirst = length - howmany  #note this is how far from end
   # upper bol bands
    # Plus closed greater than upper
    StockData['CloseGtrupper'] = StockData['Close']  - StockData['UpperBol']
    #Plus close great than upper minusx percent
    StockData['CloseGtrPlusPer'] = StockData['Close'] - StockData['UpperminusPer']

  # Lower bol bands
    # plus if close lower than lower
    StockData['CloseLowerLower'] = StockData['LowerBol']  - StockData['Close']
    # plus if close is below x per cent of Lower
    StockData['CloseLowerPlusPer'] = StockData['lowerPlusPer'] - StockData['Close']

  # Check if tight band at end
    # make a short list
    stockpricesshort = []
    stockpricesshort = StockData[lfirst : length]

    #find if there is a narrow part of the bol band
    Squeeze = False
    percent = .03    # how much from the difference (sensitivity)
    per = 1000  #load something
    count = 0   #clear count
     #find if there is a narrow part of the bol band
    for x in stockpricesshort['difBol']:
      if x < per:
        old = x
        per = old + old * percent
        count = count + 1
      else :
        count = 0
    # is there a narrow band at end of plot
    if count > 8:
      Squeeze = True

 # these are true if the condition happened in the last two samples
    howmany = 2    # redefine howmany
    lfirst = length - howmany  #note this is how far from end
    SPX = []
    SPX = StockData[lfirst : length]

    # closed above upper bollinger band
    CloseHi = False
    for x in SPX['CloseGtrupper']:
      if  CloseHi == False :        # not found yet do not clear if found
        if x > 0:
          CloseHi = True

    # closed above upper bollinger band minus 5%
    CloseHiPer = False
    for x in SPX['CloseGtrPlusPer']:
      if  CloseHiPer == False :
        if x > 0:
          CloseHiPer = True

     # closed below lower bollinger band
    CloseLow = False
    for x in SPX['CloseLowerLower']:
      if CloseLow == False :
        if x > 0:
          CloseLow = True

     # closed below lower bollinger band plus 5%
    CloseLowPer = False
    for x in SPX['CloseLowerPlusPer']:
      if  CloseLowPer == False :
        if x > 0:
          CloseLowPer = True

    Buldge = False  # not done yet
    # return bol conditions
    return(Squeeze, Buldge, CloseHi, CloseHiPer, CloseLow, CloseLowPer)
