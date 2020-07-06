from django.conf.urls import url
from .views import *
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

admin.autodiscover()
urlpatterns = [

    url(r'^$', views.index, name='index'),
    path('new_comp', views.new_comp, name='new_comp'),
    path('edit_comp/<str:id>', views.edit_comp, name='edit_comp'),
    path('enter_comp/<str:id>', views.enter_comp, name='enter_comp'),
    path('signup', views.signup, name='signup'),
    # path('<user>', views.logged_in, name='logged_in'),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html", redirect_authenticated_user=True), name='login'),
    

]
