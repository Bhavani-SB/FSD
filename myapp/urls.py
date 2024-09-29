from django.urls import path
from . import views
from .views import admin_login, admin_page
from .views import admin_view
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('mainn/', views.mainn, name='mainn'),
    path('', views.index, name='index'),  # Adding the index route here
    path('admin/', admin_view, name='admin_view'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin/', admin_page, name='admin_page'),
  
    path('about/', views.about, name='about'),
    
]