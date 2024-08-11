"""
Definition of urls for DjangoWebdata.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

#     requested  URL   view function   optional name of url
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    
    path('upload/', views.uploadfile, name='uploadfile'),
    path('junk', views.junk, name='junk'),
    path ('plotreq' , views.plotrequest, name='junkplotrequest'),
    path('plotout', views.plotout, name='plotout'),
    path('outscore', views.outscore, name='outscore'),
    # path('plottest', views.plottest, name='plottest'),
    path('dashboard/dashwatchlist', views.createwatchlist, name='dashwatchlist'),
    path('dashboard/dashownlist', views.createownlist, name='dashownlist'),
    path('dashdeletelist/<int:id>', views.dashdeletelist, name='dashdeletelist'),
    path('dashdeletelist/', views.dashdeletelist, name='dashdeletelist'),
    path('deletefile/<int:id>', views.dashdeletefile, name='dashdeletefile'),
    path('seefilelist/<int:id>', views.dashseefilelist, name='dashseefilelist'),
    path('delstk/<str:id>', views.delstk, name='delstk'), 
    path('teststockpage/', views.teststockscore, name='teststockpage'),  
    
    
    path('dashselectownlist/<int:id>', views.dashselownlist, name='seldashownlist'),
    path('dashselwatchlist/<int:id>', views.dashselwatchlist, name='seldawatchlist'),

    path ('enterownstock/<int:id>', views.enterownstock, name='enterownstock'),
    path ('enterownstock', views.enterownstock, name='enterownstock'),
    path ('enterwatchstock/<int:id>', views.enterwatchstock, name='enterwatchstock'),
    path ('enterwatchstock', views.enterwatchstock, name='enterwatchstock'),
   
    path ('dashselectownlist/plotreq' , views.plotrequest, name='plotrequest'),
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


