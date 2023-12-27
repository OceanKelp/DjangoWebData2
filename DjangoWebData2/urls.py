"""
Definition of urls for DjangoWebdata.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

#                          requested  URL      view function   optional name of url
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    
   
    # path('dashboard/dashstock/', views.createstock, name='newstock'),
    path ('dashboard/dashwatchlist', views.createwatchlist, name='dashwatchlist'),
    path ('dashboard/dashownlist', views.createownlist, name='dashownlist'),
    
    path('dashselectown/<int:id>', views.dashselownlist, name='seldashownlist'),
    path('dashselwatchlist/<int:id>', views.dashselwatchlist, name='seldawatchlist'),



    path ('enterownstock/<int:id>', views.enterownstock, name='enterownstock'),
    path ('enterownstock', views.enterownstock, name='enterownstock'),
    path ('enterwatchstock/<int:id>', views.enterwatchstock, name='enterwatchstock'),
    path ('enterwatchstock', views.enterwatchstock, name='enterwatchstock'),

    path('enterstocklist/', views.enterstocklist, name='enterstocklist'),
    path('Stocks/', views.Stocks, name='Stocks'),
    path('stockwatch/', views.stockwatch, name='stockwatch'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]


