"""
Definition of models.
"""
# passwoed for herb  Stock4Me

# python manage.py makemigrations
# python manage.py migrate
# python manage.py showmigrations
# python manage.py changepassword herb
# python manage.py createsuperuser
# python manage.py runserver

#herb
#mrherbson  thinl old

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from datetime import date
from django.contrib.auth.models import User
from django import forms

#name of stock list
class StockListNames(models.Model):
    stocklist_name = models.CharField(max_length=30)
    SLdate_registered = models.DateField()                  # register date
    userowns = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=0)

# list of stocks you own
class StockOwn(models.Model):
    stock_symbols = models.CharField(max_length=6)
    stock_name = models.CharField(max_length=6)
    stock_own = models.BooleanField()
    stock_qty = models.DecimalField(max_digits=10, decimal_places=5)
    stockdate_registered = models.DateTimeField()
    stocklist_name = models.ForeignKey(StockListNames , on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
 #list of stocks to watch   
class StockWatch(models.Model):
    watch_symbols = models.CharField(max_length=6)
    stocklist_name = models.ForeignKey(StockListNames , on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)

# file upload save name in database
class FileModel(models.Model):
    uploaded_file = models.FileField(upload_to='app.uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE ,default = 1)
    fields = ['file_field']
    
# model for score selection
class ScoreModel(forms.Form):
    OPTIONS = [
        ('50', '50'),
        ('40', '40'),
        ('30', '30'),
        ('20', '20'),
        ('10', '10'),
        ('0', '0'),
        ('-10', '-10'),
        ('-20', '-20'),
        ('-30', '-30'),
        ('-40', '-40'),
        ('-50', '-50'),
    ]
    select_field = forms.ChoiceField(choices=OPTIONS, label="Select a score")    
    

