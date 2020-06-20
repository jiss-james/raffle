from django.conf.urls import url
from .views import *
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views
admin.autodiscover()
urlpatterns = [

    url(r'^$', views.index, name='index'),
    path('new_comp', views.new_comp, name='new_comp'),
    path('edit_comp/<str:id>', views.edit_comp, name='edit_comp')

]