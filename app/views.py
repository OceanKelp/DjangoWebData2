"""
Definition of views.
"""

from datetime import datetime
from os import name
from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import redirect, render
from .forms import EnterStockListForm , StockForm, StockWatchForm
from app.databasehelper import create_stocklist
from app.databasehelper import create_owned_list
from app.databasehelper import create_stockwatch, getstockwatch,addwatchstock, set_cache_value, get_cache_value

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
            'title':'Contact',
            'message':'Your contact page.',
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
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    ) 
# ENTER STOCKLIST 
def enterstocklist(request):
    """Renders the stocklist page."""
    if request.method == 'POST':
        form = EnterStockListForm(request.POST)
        if form.is_valid():
            # Access cleaned_data only if the form is valid
            stock_list = form.cleaned_data['stocklist_name']
            ownornot= False
            personloggedin = request.user
            #create stocklist
            create_stocklist(stock_list,ownornot, personloggedin )
            return redirect('about')
        else:
            return render(request, 'app/dashboard.html', {'form': form, 'error_message': 'error.'})
    else:
        # first time page view
        form = EnterStockListForm()
        return render(
            request,
            'app/enterstocklist.html',
            {
                'title':'NewStocklist',
                'message':'Enter Your new List of stocks .',
                'year':datetime.now().year,
                'form': form, 
            }
        )
    return()
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
            'message':'Enter Your new Watch of stocks .',
            'year':datetime.now().year,
             'person' : mrX,
            'form': form, 
        }
    )
    return()

# create own list

def createownlist(request):
    assert isinstance(request, HttpRequest)
    mrX = request.user
    form = EnterStockListForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # Access cleaned_data only if the form is valid
            stock_list = form.cleaned_data['stocklist_name']
            personloggedin = request.user
            ownornot= True
            #create stocklist
            create_stocklist(stock_list,ownornot, personloggedin )
            return redirect('about')
    else:
        print(form.errors)
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
        }
    )
    return()

# enter a new owned stock in proper list
def enterownstock(request, id=0):
    assert isinstance(request, HttpRequest)
    listid = id
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
           
            return redirect('about')
        else:
            return render(request, 'app/enterownstock.html', {'form': form, 'error_message': 'error.'})
      
    return render(
        request,  
        'app/enterownstock.html', 
        {   
            'listid': listid,
            'title':'Enter a own stock',
            'message':'Add to your List of owned stocks.',
            'year':datetime.now().year,
            'form': form, 
        }
    )

    return











def Stocks(request):
    assert isinstance(request, HttpRequest)
    
    # Handle both GET and POST requests
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            # Access cleaned_data only if the form is valid
            stocks = form.cleaned_data['stock_name']
            personloggedin = request.user
            stocklist = request.stocklist
            create_owned_list(stocks, personloggedin)
            return redirect('about')
    else:
        form = StockForm()

    # Render the template with the form
    return render(
        request,
        'app/Stocks.html',
        {
            'title': 'Stocks',
            'message': 'Your Stocks page.',
            'year': datetime.now().year,
            'form': form,
        }
    )



    
# # ENTER name of list STOCKS TO WATCH PAGE
def stockwatch(request):
    assert isinstance(request, HttpRequest)
    """Renders the stocklist page."""
    form =StockWatchForm(request.POST)
    
    if request.method == 'POST':
       
        form = StockWatchForm(request.POST)
        if form.is_valid():
            # Access cleaned_data only if the form is valid
            stock_list = form.cleaned_data['stockwatch_name']
            personloggedin = request.user
            create_stockwatch(stock_list,personloggedin )
               
            return redirect('about')
        else:
            return render(request, 'app/register.html', {'form': form, 'error_message': 'error.'})
      
    return render(
        request,
        'app/stockwatch.html',
        {
            'title':'stockwatch',
            'message':'Your List of stocks to watch page.',
            'year':datetime.now().year,
            'form': form, 
        }
    )




    
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
#example
# views.py
from django.shortcuts import render
from .models import StockWatch



from .models import StockListNames
from app.databasehelper import getstocklist


    


# get list of list  out[ut not used input is working sample]
def dashselownlist(request, id):
    assert isinstance(request, HttpRequest)
    IDback = id
    return render( 
        request,
        'app/about.html',
        {
            # 'username': capitalized_username,
            'title': IDback,
            'message': 'Your dashboard is used to select, create, and edit (watch lists and owned Lists.',
            'year': datetime.now().year,  
        }
    )
    return()
    
def dashselwatchlist(request, id):
    pass
    return()

def dashboard(request):
    """Renders the dashboard."""
    assert isinstance(request, HttpRequest)
    # Assuming you have a logged-in user

    user_id = request.user.id
    capitalized_username =  capitalized_username = request.user.username.upper()  # make name caps for display

    # Retrieve the StockList for the user
    # try:
    #     stock_list = StockListNames.objects.get(user_id=user_id)
    # except StockListNames.DoesNotExist:
    #     stock_list = None
    alllist = getstocklist(user_id)
    return render( 
        
        request,
        'app/dashboard.html',
        {
            'username': capitalized_username,
            'title': 'DASHBOARD',
            'message': 'Your dashboard is used to select, create, and edit (watch lists and owned Lists.',
            'year': datetime.now().year,
            'showstock': alllist,
        }
    )


()
def dashselownlist(request, id):
    # herb working here
    returen()





# To save a session variable
def save_session_var(request):
    request.session['my_var'] = 'Hello, World!'

# To get a session variable
def get_session_var(request):
    my_var = request.session.get('my_var', 'Default Value')
    return my_var

# def xtab1_view(request):
    
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/tab1_view.html',
#         {
#             'title':'Tab1',
#             'message':'Your application description page.',
#             'year':datetime.now().year,
#         }
#     )


# def xtab2_view(request):
#     """Renders the about page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/tab2_view.html',
#         {
#             'title':'tab1',
#             'message':'Your application description page.',
#             'year':datetime.now().year,
#         }
#     )

