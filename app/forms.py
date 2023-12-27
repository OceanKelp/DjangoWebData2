"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
  
   #stocklist name
class EnterStockListForm(forms.Form):
    stocklist_name = forms.CharField(max_length=30,  widget=forms.TextInput({
                                'class': 'form-control',
                                'placeholder': 'StockList name'}))
    # ownnot = forms.BooleanField(widget=forms.CheckboxInput({
    #                     'class': 'form-control',
    #                     'placeholder': 'Iown'})) 
       



  #stocks you own name
class StockForm(forms.Form):
   
    stock_symbols = forms.CharField(max_length=6,
                                widget=forms.TextInput({
                        'class': 'form-control',
                        'placeholder': 'StockList name'}))
        
    # stock_name = forms.CharField(max_length=30,
    #                         widget=forms.TextInput({
    #                     'class': 'form-control',
    #                     'placeholder': 'StockList name'}))
        
    # stock_own = forms.BooleanField(widget=forms.CheckboxInput({
    #                     'class': 'form-control',
    #                     'placeholder': 'stock_own'})) 
    stock_qty = forms.DecimalField(max_digits=10, decimal_places=2,
                                    widget=forms.TextInput({
                        'class': 'form-control',
                        'placeholder': 'StockList name'}))
    
     
class StockWatchForm(forms.Form):
    stockwatch_name = forms.CharField(max_length=30,  widget=forms.TextInput({
                                'class': 'form-control',
                                'placeholder': 'stockwatch name'}))
             


