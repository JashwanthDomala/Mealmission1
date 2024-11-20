from django.contrib import admin
from django.urls import path,include
from . import views as v
app_name='base'
urlpatterns = [
   path('',v.home,name='home'),
   path('org/',v.org,name='org'),
   path('add/',v.add,name='add'),
   path('delete/',v.delete,name='delete'),
   path('food/update/<int:pk>/', v.update_food, name='update_food'),
   path('vol/',v.vol,name='vol')
]
