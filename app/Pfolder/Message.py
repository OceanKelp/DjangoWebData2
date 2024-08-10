
from app.Pfolder.Bol import Bollinger
from app.Pfolder.Conditions import JustChanged
#put together a message
def StatusMessage(SPL , SymbolIn):
  # setup
  GoodPoints = 0
  BadPoints = 0
  StatusMessageBad = ''
  StatusMessageGood =''

  # Bolinger Bands
  Squeeze, Buldge, CloseHi, CloseHiPer, CloseLow, CloseLowPer  = Bollinger(SPL, SymbolIn)

  if Squeeze :
    StatusMessageGood = ' Squeeze'
    GoodPoints = GoodPoints + 15

  if CloseHi:
    StatusMessageGood = StatusMessageGood + ' Close Above  Bolinger U '
    GoodPoints = GoodPoints + 15

  if CloseHiPer:
    StatusMessageGood = StatusMessageGood + ' Close Above Bolinger UP '
    GoodPoints = GoodPoints + 5

  if CloseLow:
    StatusMessageBad = StatusMessageBad + ' Close Below Bolinger L '
    BadPoints =  BadPoints + 15

  if CloseLowPer:
    StatusMessageBad = StatusMessageBad + ' Close Below Bolinger L P '
    BadPoints =  BadPoints + 10

# Moving average

  CloseAlreadyBelow20  , CloseJustWentBelow20 , CloseJustWentAbove20 , CloseBeenAbove20 ,\
  CloseAlreadybelow50 ,  CloseJustWentBelow50 , CloseJustWentAbove50 , CloseBeenAbove50 , \
  MA20AlreadyBelow50MA , MA20JustWentBelow50MA , MA20JustWentAbove50MA  , MA20BeenAbove50MA = JustChanged(SPL, SymbolIn)

  # closed below MA20
  if CloseAlreadyBelow20:
    StatusMessageBad = StatusMessageBad + ' Closed Below MA20 '
    BadPoints =  BadPoints + 5
   # Just closed below mA20
  if CloseJustWentBelow20:
    StatusMessageBad = StatusMessageBad + ' Just Closed Below MA20 '
    BadPoints =  BadPoints + 10
   # just closed above MA20
  if CloseJustWentAbove20:
    StatusMessageGood = StatusMessageGood + ' Just Closed Above MA20 '
    GoodPoints = GoodPoints + 10
  # closed been above MA20
  if CloseBeenAbove20:
    StatusMessageGood = StatusMessageGood + ' Closed Above MA20 '
    GoodPoints = GoodPoints + 5


  # closed below MA50
  if CloseAlreadybelow50:
    StatusMessageBad = StatusMessageBad + ' Closed Below MA50 '
    BadPoints =  BadPoints + 15
  # Just closed below mA50
  if CloseJustWentBelow50:
    StatusMessageBad = StatusMessageBad + ' Just Closed Below MA50 '
    BadPoints =  BadPoints + 20
 # cjust losed abovr ma 50
  if CloseJustWentAbove50:
    StatusMessageGood = StatusMessageGood + ' Just Closed Above MA50 '
    GoodPoints = GoodPoints + 10
  # just closed above MA50
  if CloseBeenAbove50:
    StatusMessageGood = StatusMessageGood + ' Closed Above MA50 '
    GoodPoints = GoodPoints + 10

    # 20 day below 50 day
  if MA20AlreadyBelow50MA:
    StatusMessageBad = StatusMessageBad + '  MA20 is below MA50 '
    BadPoints =  BadPoints + 20
  # MA20 went below MA50
  if MA20JustWentBelow50MA:
    StatusMessageBad = StatusMessageBad + '  MA20 just went below MA50 '
    BadPoints =  BadPoints + 25
  # MA20 just went above ma50
  if MA20JustWentAbove50MA:
    StatusMessageGood = StatusMessageGood + ' MA20 just went above ma50 '
    GoodPoints = GoodPoints + 10
   # 20 day below 50 day
  if MA20BeenAbove50MA:
    StatusMessageBad = StatusMessageBad + '  MA20 is above MA50 '
    GoodPoints =  GoodPoints + 5

  return(StatusMessageGood , StatusMessageBad ,GoodPoints , BadPoints )
