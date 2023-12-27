"""
Definition of models.
"""

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from datetime import date





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

