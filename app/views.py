"""
Definition of views.
"""

from asyncio.windows_events import NULL
from datetime import datetime
from email.policy import default
from operator import index
from os import name
from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import redirect, render
from .forms import EnterStockListForm , StockForm, StockWatchForm,teststockForm
from app.databasehelper import create_stocklist
from app.databasehelper import create_owned_list,getlistname
from app.databasehelper import create_stockwatch, getstockwatch,addwatchstock, set_cache_value, get_cache_value
from .models import StockWatch
from .models import StockListNames, FileModel
from .models import ScoreModel
from app.databasehelper import getstocklist,getownedstock,get_uploaded_files,deleteuploadfile,getfileinfo
from app.databasehelper import get_value, save_key_value_pair
from app.forms import FileForm
from app.Pfolder.StkRwelve import RunUserList      
from app.Pfolder.GetUserFile import GetFileUpload
import pandas as pd
import numpy as np
from app.Pfolder.GetBatchData import GetBatchDataRT
from app.Pfolder.GetFile import readcsv
from app.Pfolder.StockHandler import handletocks
from app.databasehelper import save_key_value_pair, get_value, set_user_cache, get_user_cache,delete_stock_symbol
from django.views import View
from django.http import JsonResponse
from app.Pfolder.Error import errorhandler
import json


# home page
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

# contact page
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'MY nonContact',
            'message':'as of yet i do not have an email',
            'year':datetime.now().year,
        }
    )

# about page
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About FUN',
            'message':'Have fun while learn.',
            'year':datetime.now().year,
        }
    ) 
    
#create watchlist
def createwatchlist(request):
    assert isinstance(request, HttpRequest)
    mrX = request.user
    form = EnterStockListForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # Access cleaned_data only if the form is valid
            stock_list = form.cleaned_data['stocklist_name']
            personloggedin = request.user
            ownornot= False
            #create stocklist
            create_stocklist(stock_list,ownornot, personloggedin )
            return redirect('about')
    else:
        # first time page view
        form = EnterStockListForm()
    return render(
        request,
        'app/dashwatchlist.html',
        {
            'title':'New Watch List',
            'message':'Enter Your new Watch list name.',
            'year':datetime.now().year,
            'person' : mrX,
            'form': form, 
        }
    )
    return()

# create own list
def createownlist(request):
    assert isinstance(request, HttpRequest)
    duperror = None
    mrX = request.user
    form = EnterStockListForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # Access cleaned_data only if the form is valid
            stock_list = form.cleaned_data['stocklist_name']
            personloggedin = request.user
            ownornot= True
            
            existing_list = StockListNames.objects.filter(stocklist_name=stock_list, user=personloggedin).exists()
           # existing_list = StockListNames.objects.filter(name=stock_list, user=personloggedin).exists()

            if existing_list:
                # If a list with the same name exists, inform the user and do not create a new list
                duperror = 'A list with this name already exists. Please choose a different name.'
            else:
                # If no such list exists, proceed to create the stock list


                #create stocklist
                create_stocklist(stock_list,ownornot, personloggedin )
                return redirect('dashboard')
    else:
        # first time page view
        form = EnterStockListForm()
    return render(
        request,
        
        'app/dashownlist.html',
        {
            'title':'Enter name of the list of stocks you OWN',
            'message':'Enter Your new Owned list name.',
            'year':datetime.now().year,
            'person': mrX,
            'form': form, 
            'error_message': duperror
        }
    )
    return()


def delstk(request, id):  # id is the stock symbol
        code='azx'
        listid = get_user_cache(request.user, 'listid' + code,)
        delete_stock_symbol(request,listid,id)
        return redirect('dashboard')
    

def enterownstock(request, id=0): # id is the list id
    assert isinstance(request, HttpRequest)
    listid = id
    code='azx'
    set_user_cache(request.user , 'listid' + code, listid, )
    thisownlist = getownedstock(id,request.user.id)  # get list of owned stocks
    
    # Check if thisownlist is not empty and set default values if it is empty
    if thisownlist:
        oldstocks, stock_qty = zip(*thisownlist)  # unpack tuple
        str_var = " ".join(oldstocks)  # convert tuple to string
    else:
        # Set default values if thisownlist is empty
        oldstocks, stock_qty = [], []
        str_var = ""
    str_var = str_var.upper()           # make name caps for display
    # Create a string of stock symbols with hyperlinks to select the stock
    stk =' '
    for s in oldstocks: 
        s = s.upper()
        stk = stk + '<a href="/delstk/' + s + '">' +s +'</a>   '
    form =StockForm(request.POST)   
    if request.method == 'POST':

        form = StockForm(request.POST)
        if form.is_valid():
            # Access cleaned_data only if the form is valid
            stock_symbols = form.cleaned_data['stock_symbols']
            stockname = 'na'
            stock_own = True
            stock_qty = form.cleaned_data['stock_qty']
            #stockdate_registered = datetime.now()
            stocklist_name = StockListNames.objects.get(id= listid)              
            user = request.user
            create_owned_list(stock_symbols, stockname,stock_qty,stocklist_name,user)
            return render(request, 'app/enterownstock.html', {'form': form, 'error_message': 'error.'})
          ###  return redirect('about')
        else:
            return render(request, 'app/enterownstock.html', {'form': form, 'error_message': 'error.'})
      
    return render(
        request,  
        'app/enterownstock.html', 
        {   
            'listid': listid,
            'title': 'Enter a own stocks  ',
            'message': 'Presently owned stock ' + str_var,
            'year':datetime.now().year,
            'del': 'Delete stock from list  ' + stk,
            'form': form, 
        }
    )

    return

  
# enter a new watch stock in proper list
def enterwatchstock(request, id=0):
    assert isinstance(request, HttpRequest)
    listid = id
    form =StockWatchForm(request.POST)   
    if request.method == 'POST':
       
        form = StockWatchForm(request.POST)
        if form.is_valid():
            # Access cleaned_data only if the form is valid
            stock_list = form.cleaned_data['stockwatch_name']
            personloggedin = request.user
            stocklist_name = listid #get_cache_value('listid')
            addwatchstock( stock_list ,stocklist_name,personloggedin )
               
            return redirect('about')
        else:
            return render(request, 'app/enterwatchstock.html', {'form': form, 'error_message': 'error.'})
      
    return render(
        request,  
        'app/enterwatchstock.html', 
        {   
            'listid': listid,
            'title':'Enter a watch stock',
            'message':'Add to your List of stocks to watch .',
            'year':datetime.now().year,
            'form': form, 
        }
    )

    return


#Dashboard
def dashboard(request):
    """Renders the dashboard."""
    assert isinstance(request, HttpRequest)
    user_id = request.user.id
    capitalized_username =  capitalized_username = request.user.username.upper()  # make name caps for display
    # Retrieve the StockList for the user owned and watch list
    alllist = getstocklist(user_id)
    #retrive the stock file names and file ID
    filelist = get_uploaded_files(request.user.id)
    # select the minimum score
    form = ScoreModel
    # make sure a minimum score is selected
    errmess = errorhandler('MinError',request)  
    # Handle form submission
    if request.method == 'POST':
        form = ScoreModel(request.POST)
        if form.is_valid():
            selected_option = form.cleaned_data['select_field']
            save_key_value_pair(request,'MinScore',selected_option)
            # Save the selected option 
    else:
        minscore = get_value(request, 'MinScore')
        form = ScoreModel(initial={'select_field': minscore ,default: -60})
    return render( 
        
        request,
        'app/dashboard.html',
        {
            'error_message': errmess,
            'username': capitalized_username,
            'title': 'DASHBOARD',
            'message': 'Your dashboard is used to select, create, and edit (watch lists and owned Lists.',
            'year': datetime.now().year,
            'showstock': alllist,
            'fileshow': filelist,
            'form': form  # Include the form in the context
        }
    )


# select owned stock from a certain list 
def dashselownlist(request, id): #id is the list id
   
    thisownlist = getownedstock(id,request.user.id)
    listname = getlistname  (id,request.user.id )
    person = request.user
    capitalized_person = person.username.capitalize()
    # Unzip the list of tuples into two lists
    stock_symbols, stock_qty = zip(*thisownlist)  
    stock_qty = [round(qty) for qty in stock_qty]  
    stock_symbolslist = list(stock_symbols)
   
    # Assuming stock_symbolslist is a list of strings
    stock_symbolslistC = [symbol.upper() for symbol in stock_symbolslist]

    DFOut, stkdata,Smalldf2 = handletocks(stock_symbolslistC ,request)
    sym = DFOut['symbol'].tolist()
    sym_str = ' '.join(map(str, sym))
     
    output = []
    output = iterateRow2(DFOut,request)  
    
    return render( 
        request,
        'app/dashselownlist.html',
        {
            'username': capitalized_person,
            'list': listname,
            'title': 'Owned List ' ,   
            'info':  ' symbol  score, ',
            'year': datetime.now().year,
            'clickstocks': 'dashselownlist',
            'scores':output,
            'qty': stock_qty
        }
    )
    return()



   # get watch list
def dashselwatchlist(request, id): # id is the list id
    thiswatchlist = getstockwatch(id,request.user.id)
    listname = getlistname  (id,request.user.id )
    person = request.user
    capitalized_person = person.username.capitalize()  
    stock_symbolslist = list(thiswatchlist)
   
    # Assuming stock_symbolslist is a list of strings
    stock_symbolslistC = [symbol.upper() for symbol in stock_symbolslist]

    DFOut, stkdata,Smalldf2 = handletocks(stock_symbolslistC ,request)
    sym = DFOut['symbol'].tolist()
    sym_str = ' '.join(map(str, sym))
     
    output = []
    clickbait = iterateRow2(DFOut, request)
        
    return render(request, 'app/outscore.html',
        {
            'title': 'scores of stocks       click symbol for chart',
            'message': clickbait ,  # this is the click on symbol that is greater than limit
            'symbol': sym_str,   # this is the list of symbols
            'score': output, # this is big nessage closed aboved or below message
            'year': datetime.now().year,
        }    
        )

# delete list
def dashdeletelist(request, id=None):
    if id is None:   #this is the return from warning
        id  = get_value(request, 'listid')
        userx =  request.user.id
        stock_list_instance = StockListNames.objects.get(id=id, user=userx)

        # Delete the instance
        stock_list_instance.delete()
        return redirect('dashboard')

    else:
        # Handle the case where id is passed
        listname = getlistname(id,request.user.id )
        save_key_value_pair(request, listname,listname)
        save_key_value_pair(request,'listid',id)
        return render( 
        
        request,
        'app/dashdeletelist.html',
        {
            'title': 'delete List',
            # 'username': capitalized_person,
            'message1': 'Caution all the stocks in the',
            'list': listname,
            'message': ' will be deleted.',          
        }
        )

# delete file
def dashdeletefile(request, id): # id is the file id           
            message = deleteuploadfile(request.user.id, id)
            if message == 'deleted':
                return redirect('app.dashboard')
            else:
                return redirect('about')# this error message  herb

# call with file id and the on click and score will be returend
# this gets new data from internet  herb add look for old data
def dashseefilelist(request,id):  #id is file id
    file_path = getfileinfo(request.user.id,id)  # need to get file path and file name
    pathpre =  'C:/Users/herb/VS23/DjangoWebData2/'
    file_name = pathpre + file_path     
    df = pd.read_csv(file_name)         #read selected scorefile
    content = df['Symbol']
    Clist = content.tolist()            # create list of symbols
    DFOut , DataOut , smalldf2x = handletocks(Clist,request) # get new data
    sym = DFOut['symbol'].tolist()
    sym_str = ' '.join(map(str, sym))
    # make symbol clickable
    clickbait = iterateRow2(DFOut, request)
    error_condition = True  # This should be replaced with your actual error condition check

    
    return render(request, 'app/outscore.html',
    {
        'title': 'scores of stocks       click symbol for chart',
        'message': clickbait ,  # this is the click on symbol that is greater than limit
        'symbol': sym_str,   # this is the list of symbols
        'score': DataOut, # this is big nessage closed aboved or below message
        'year': datetime.now().year,
    }    
    )

def newrow():
        return("</tr>  ")
def endrow():
        return("</td> <tr> <td>")    
 
    
def iterateRow2(dfin,request):
    output = []
    count = 0
    for index, row in dfin.iterrows():
        

        minscore = int(get_value(request, 'MinScore'))  # Convert to integer
        if row['score'] > minscore: 
        
            pair = f'<span id="{index}" onclick="CallBackF({index}, \'{row["symbol"]}\')">{row["symbol"]} {row["score"]}</span> '
            output.append(pair)
            if count >= 9:
                output.append(endrow())
                count = 0
            else:  
                count = count + 1
    # You can add more code here to do other things with 'index' and 'row'
    output.append(endrow() )         
    output = ',  '.join(output)
    return(output)

 
def teststockscore(request):
    assert isinstance(request, HttpRequest)
    form = teststockForm(request.POST)
   
    if request.method == 'POST':  
       # form = teststockForm(request.POST)
        if form.is_valid():
            personloggedin = request.user
          
            stock_data = [form.cleaned_data['Stock_1'].upper(),
                          form.cleaned_data['Stock_2'].upper(), 
                          form.cleaned_data['Stock_3'].upper(), 
                          form.cleaned_data['Stock_4'].upper(), 
                          form.cleaned_data['Stock_5'].upper()]
            # remove blanks
            stock_data = [stock for stock in stock_data if stock != '']  
            # remove duplicates
            stock_data = list(set(stock_data))
            # Sort the list in alphabetical order
            stock_data.sort()
            # get the data
            dfScore, DataOut , smalldf2x = handletocks(stock_data,request)            # put data in json format
            smalldfjson = smalldf2x.to_json(orient='records', default_handler=str)
            click = iterateRow2(dfScore,request )   
            save_key_value_pair(request,'Click',click)   
            save_key_value_pair(request,'DataOut',DataOut)                        
            save_key_value_pair(request,'dfsmall',smalldfjson)  
                      
            return redirect('outscore') ##
        else:
            return render(request, 'app/teststockpage.html', {'form': form, 'error_message': 'error.'})
      
    return render(
        request,  
        'app/teststockpage.html', 
        {      
            'title':'Enterk',
            'message':'enter stock to test the score.',
            'year':datetime.now().year,
            'form': form, 
        }
    )

def outscore(request):
     return render(
        request,  
        'app/outscore.html',   
        {   
            'title':'the present stock score',
            'message': (get_value(request,'Click')), 
            'year':datetime.now().year,
            'score': get_value(request,'DataOut'), #this is data to show
        }
    )
    

def junk(request):
    symbol = "BIO"
    jd = get_value(request, symbol)
  #  id = request.user.id  gets user id number
     #id = request.user gets the user name
   
    assert isinstance(request, HttpRequest)
    return render( request, 'app/junk.html', 
    {
        'json_data': jd,
        'title':'junk',
        'message':'Your junk application description page.',
        'year':datetime.now().year,
        'stock': symbol,
    }
    ) 

# upload file
def uploadfile(request):
    if request.method == 'POST':
        # Change the variable name to avoid naming conflict
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # Create an instance of the model but don't save it yet
            file_model_instance = FileModel(uploaded_file=form.cleaned_data['uploaded_file'], user=request.user)
            # Now save the model instance
            file_model_instance.save()

            # Redirect to a success page or do other actions
            # herb change redirect to a page that shows the sussessful upload
            return redirect('about')
        else:
            return render(request, 'app/uploadfile.html', {'form': form, 'error_message': 'Not a valid file.'})
    else:
        # If it's a GET request, create an empty form
        form = FileForm()
        return render(request, 'app/uploadfile.html', {'message': 'Upload file', 'title': 'Load file', 'form': form})
 
def plotout(request):
        chart_data = get_value(request, 'C')  # Replace with your actual chart data
        return render(request, 'app/plotout.html', {'chart_data': chart_data})


def plotx(request,symbol,pathin):
     chart_data = get_value(request, symbol) 
     return render(request, pathin, {'chart_data': chart_data})



def plotrequest(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        index = data.get('index')
        symbol = data.get('symbol')
        # pathx = request.path
  
        # jd = get_value(request, symbol) 
        # chart_data = get_value(request, symbol) 
      #  chart_data_dict = json.loads(chart_data)
      #  return JsonResponse(chart_data_dict,safe=False)
        jd = get_value(request,symbol)
   
        return JsonResponse(jd,safe=False)

        
     
# def plottest(request):
#     assert isinstance(request, HttpRequest)
#     jd = get_value(request, 'BIO')
#   #  id = request.user.id  gets user id number
#      #id = request.user gets the user name
#     #jd = "data json"
#     assert isinstance(request, HttpRequest)
#     return render( request, 'app/plottest.html', 
#     {
        
#         'title':'testplot',
#         'message':'Your plot testing page.',
#         'year':datetime.now().year,
#         'error_message': 'error.',
#     })

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
    

