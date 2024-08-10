# these are error messages 
# It only handles one error at a time
# MinError = "Select a minimun score"
# SomeError = 'Some error'

from app.databasehelper import get_value, save_key_value_pair

def errorhandler(error, request):
    ErrorOut = None
    if error == 'MinError':
       ErrorOut = minscore(request)
    elif error == 'SomeError':  # example of another error
       ErrorOut = 'call some function'
    return(ErrorOut)   

def minscore(request):
    #make sure a minimum score is selectet
   errmess  = get_value(request, 'MinScore') 
   if errmess == None:
       errmess = "Select a minimun score" 
   else: 
       errmess = None    
   return(errmess)