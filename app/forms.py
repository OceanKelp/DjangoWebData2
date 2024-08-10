"""
Definition of forms.
"""
from .models import FileModel
from stat import filemode
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
import mimetypes
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
import csv

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
            

# used for to test stock score
class teststockForm(forms.Form):
    Stock_1 = forms.CharField(required=True)
    Stock_2 = forms.CharField(required=False)
    Stock_3 = forms.CharField(required=False)
    Stock_4 = forms.CharField(required=False)
    Stock_5 = forms.CharField(required=False)


class FileForm(forms.Form):
    uploaded_file = forms.FileField()

    def clean_uploaded_file(self):
        uploaded_file = self.cleaned_data.get('uploaded_file')
        # Use the name attribute of the file to get the filename
        file_name = uploaded_file.name
        # Check if the file has a CSV extension
        if not file_name.endswith('.csv'):
            raise forms.ValidationError("Only CSV files are allowed.")

        return uploaded_file
