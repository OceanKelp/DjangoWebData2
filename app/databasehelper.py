from datetime import date
from datetime import datetime
from typing import Self
from .models import  StockListNames, StockOwn, StockWatch, FileModel
import numpy as np
import os

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
           # stocklist_name = StockListNames.objects.get(id=stocklistin),
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
   
    # stocklist_id = stocklistin
    # user_id = user_idin      
    # Query to get all stock_symbols for a specific StockList and User
    stock_watch_list = StockWatch.objects.filter(
        user=user_idin,
        stocklist_name=stocklistin
        ).values_list('watch_symbols', flat=True)
    # Convert the queryset to a Python list
    stock_symbols = list(stock_watch_list)
    stock_symbols.sort()
    return(stock_symbols)

# returns a list of stock_symbols for a specific StockList and User
def getownedstock(stocklistIDin,user_idin):  
    
    stock_owned_list = StockOwn.objects.filter(
        user=user_idin,
        stocklist_name=stocklistIDin
        ).values_list('stock_symbols', 'stock_qty')

    # Convert the queryset to a Python list
    stock_info = list(stock_owned_list)
    stock_info.sort()
    return(stock_info)


def save_key_value_pair(request, key, value):
    request.session[key] = value
    return None


def get_value(request, key):
    try:
        value = request.session[key]
    except KeyError:
        value = None
    return value




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



# get list name 
def getlistname(stocklist_id,user_idin,):
    # Query to get the stocklist_name for a specific StockListNames instance and User
    stock_list_name = StockListNames.objects.filter(
        user_id=user_idin,
        id=stocklist_id
        ).values('stocklist_name').first()
    # If the StockListNames instance exists, return the stocklist_name, else return None
    return stock_list_name['stocklist_name'] if stock_list_name else None


def getstocklist(user_idin):
    # Query to get all stocklist_id for a specific User
    stock_list = StockListNames.objects.filter(
        user_id=user_idin,
        ).values_list('id','stocklist_name', 'userowns')
    stock_list2list = list(stock_list)
    # Now, stock_list contains a list of tuples, where each tuple is (stocklist_id, stock_symbols)
    return stock_list2list


def get_uploaded_files(user):
    files = FileModel.objects.filter(user=user).values_list('id', 'uploaded_file')
    filelist = [(file_id, file_path.replace('app.uploads/', '')) for file_id, file_path in files]
    return filelist

def deleteuploadfile(user, fileid):
    # first get data
    file_path = getfileinfo(user,fileid)  # need to get file path and file name
    pathpre =  'C:/Users/herb/VS23/DjangoWebData2/'
    file_path = pathpre + file_path
    # delete file
    if os.path.isfile(file_path):
            os.remove(file_path)
    file_to_delete = FileModel.objects.get(user=user, id=fileid)
    file_to_delete.delete()  # This will delete the record rom the database
    return('deleted')

def getfileinfo(user, fileid):
    try:
        fileinfo = FileModel.objects.get(user=user, id=fileid)
        return fileinfo.uploaded_file.url  # Assuming you want the URL of the uploaded file
    except FileModel.DoesNotExist:
        return None  # Handle the case when the file is not found


from .models import StockOwn, StockListNames, User

def delete_stock_symbol(request, listID, symbol):
    symbol = symbol.upper()
    userin = request.user.id
    stock_list = listID

   # Fetch the stock instance
   # stock_instance = StockOwn.objects.get(stock_symbols=symbol, stocklist_name=stock_list, user=userin)
    stock_instance = StockOwn.objects.filter(stock_symbols__iexact=symbol, stocklist_name=stock_list, user=userin).first()

    # Delete the instance
    stock_instance.delete()
    return None


   


from django.core.cache import cache

# Set a value in the cache
def set_cache_value(key, value):
    cache.set(key, value)
#cache.set('my_var', 'Hello, World!')



# Retrieve the value from the cache in another request
def get_cache_value(key):
    return cache.get(key)
#my_var = cache.get('my_var', 'Default Value')


def set_user_cache(user_id, key, value):
    cache_key = f"user_{user_id}_{key}"
    cache.set(cache_key, value)


def get_user_cache(user_id, key):
    cache_key = f"user_{user_id}_{key}"
    value = cache.get(cache_key)
    return value
