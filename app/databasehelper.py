from datetime import date
from datetime import datetime
from typing import Self
from .models import  StockListNames
from .models import  StockOwn
from .models import StockWatch

# save  a new STOCK LIST NAME
def create_stocklist(stocklistname,ownsin,personin):
        stocklistName = StockListNames  (
        stocklist_name = stocklistname,
        SLdate_registered = datetime.now(),
        userowns = ownsin,
        user_id = personin.id
        )
        #Save 
        stocklistName.save()
        return (stocklistname)



# Save a new watch stock
def addwatchstock(stocksymin, stocklistin, personin):
    stocksname = StockWatch(
        watch_symbols=stocksymin,
        stocklist_name=  StockListNames.objects.get(id=stocklistin),     # assuming a is an instance of StockListNames
        user=personin  # assuming personin is an instance of User
    )
    # Save
    stocksname.save()
    return stocksname




# save  owned stocks
def create_owned_list(stocksymin,stocknamein,stockqtyin,stocklistin,personin):
        stocksnameinstance = StockOwn   (
            stock_symbols = stocksymin,
            stock_name = stocknamein,
            stock_own = True,
            stock_qty = stockqtyin,
            stockdate_registered = datetime.now(),
            stocklist_name = stocklistin,#StockListNames.objects.get(id=stocklistin),
            user = personin
        )
            #Save 
        stocksnameinstance.save()
        return (stocksymin)



# create_stockwatch

def create_stockwatch(stockwatchname,personin):
        stockwatchName = StockWatch  (
        stockwatch_name = stockwatchname,
        user_id = personin.id
        )
        #Save 
        stockwatchname.save()
        return (stockwatchname)


# Retrieve all stock_symbols in specific stock watch list
def getstockwatch(stocklistin,user_idin):
    # Assuming you have the stocklist_id and user_id values
    # stocklist_id = stocklistin
    # user_id = user_idin      
    # Query to get all stock_symbols for a specific StockList and User
    stock_watch_list = StockWatch.objects.filter(
        user_id=user_idin,
        stocklist_id=stocklistin
        ).values_list('stock_symbols', flat=True)
    # Convert the queryset to a Python list
    stock_symbols = list(stock_watch_list)
    # Now, stock_symbols contains a list of all stock_symbols for the specified StockList and User
    return(stock_symbols)


#get stock  in stock watch list 
# def getstocklist(user_idin):
#     # Assuming you have the stocklist_id and user_id values
#     # stocklist_id = stocklistin
#     # user_id = user_idin      
#     # Query to get all stock_symbols for a specific StockList and User
#     stock_watch_list = StockWatch.objects.filter(
#         user_id=user_idin,
#         ).values_list('stock_symbols', flat=True)
#     # Convert the queryset to a Python list
#     stock_symbols = list(stock_watch_list)
#     # Now, stock_symbols contains a list of all stock_symbols for the specified StockList and User
#     return(stock_symbols)



#get stock  in stock watch list 
def getcertainlist(user_idin, stocklist_id):
    # Query to get all stock_symbols for a specific StockList and User
    stock_watch_list = StockWatch.objects.filter(
        user_id=user_idin,
        stocklist_id=stocklist_id
        ).values_list('stock_symbols', flat=True)
    # Convert the queryset to a Python list
    stock_symbols = list(stock_watch_list)
    # Now, stock_symbols contains a list of all stock_symbols for the specified StockList and User
    return(stock_symbols)







def getstocklist(user_idin):
    # Query to get all stocklist_id for a specific User
    stock_list = StockListNames.objects.filter(
        user_id=user_idin,
        ).values_list('id','stocklist_name', 'userowns')
    # Convert the queryset to a Python list of tuples
    stock_list2list = list(stock_list)
    # Now, stock_list contains a list of tuples, where each tuple is (stocklist_id, stock_symbols)
    return stock_list2list



# def getstocklist(user_idin):
#     # Query to get all stock_symbols and stocklist_id for a specific User
#     stock_list = StockWatch.objects.filter(
#         user_id=user_idin,
#         ).values_list('id', 'stock_symbols')
#     # Convert the queryset to a Python list of tuples
#     stock_list2list = list(stock_list)
#     # Now, stock_list contains a list of tuples, where each tuple is (stocklist_id, stock_symbols)
#     return stock_list2list




from django.core.cache import cache

# Set a value in the cache
def set_cache_value(key, value):
    cache.set(key, value)
#cache.set('my_var', 'Hello, World!')

# Retrieve the value from the cache in another request
def get_cache_value(key):
    return cache.get(key)
#my_var = cache.get('my_var', 'Default Value')