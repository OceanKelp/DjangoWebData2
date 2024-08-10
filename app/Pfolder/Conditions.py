

from app.Pfolder.Change import TestChange


# test for differnt contidtions
def JustChanged(twoday, symin):
  CloseAlreadyBelow20  = CloseJustWentBelow20 = CloseJustWentAbove20 = CloseBeenAbove20 =  False
  CloseAlreadybelow50 =  CloseJustWentBelow50 = CloseJustWentAbove50 = CloseBeenAbove50 = False
  MA20AlreadyBelow50MA = MA20JustWentBelow50MA = MA20JustWentAbove50MA  = MA20BeenAbove50MA =  False

  length = len(twoday) # change length of array
  Dayreferance = length - 2  #note this is how far from end
  stockprices2day = []
  twoday['CloseMinusMA20'] = twoday['Close'] - twoday['MA20']
  twoday['CloseMinusMA50'] = twoday['Close'] - twoday['MA50']
  #twoday['SMA50MinusMA20'] = twoday['MA50'] - twoday['MA20']
  twoday['SMA20MinusMA50'] = twoday['MA20'] - twoday['MA50']

  stockprices2day = twoday[Dayreferance : length]

  #test close and MA20
  CloseAlreadyBelow20   , CloseJustWentBelow20 , CloseJustWentAbove20  , CloseBeenAbove20 = TestChange(stockprices2day, 'CloseMinusMA20' )
  #test close and MA50
  CloseAlreadybelow50 , CloseJustWentBelow50 , CloseJustWentAbove50 , CloseBeenAbove50 = TestChange(stockprices2day , 'CloseMinusMA50' )
  # test ma50 & 20
  MA20AlreadyBelow50MA  , MA20JustWentBelow50MA , MA20JustWentAbove50MA  , MA20BeenAbove50MA = TestChange(stockprices2day, 'SMA20MinusMA50' )

# do the tests
  return(CloseAlreadyBelow20  , CloseJustWentBelow20 , CloseJustWentAbove20 , CloseBeenAbove20 , \
         CloseAlreadybelow50 ,  CloseJustWentBelow50 , CloseJustWentAbove50 , CloseBeenAbove50 , \
         MA20AlreadyBelow50MA , MA20JustWentBelow50MA , MA20JustWentAbove50MA  , MA20BeenAbove50MA   )
