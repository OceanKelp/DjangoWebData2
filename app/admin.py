from django.contrib import admin
from .models import  StockListNames, StockOwn, StockWatch, FileModel




admin.site.register(FileModel)
admin.site.register(StockListNames)      # list of stocks
admin.site.register(StockOwn)       # list of stocks you own
admin.site.register(StockWatch)    # list of stocks to watch

