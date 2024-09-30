from django.urls import path
from . import views
from .views import admin_login, admin_page, admin_view

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('mainn/', views.mainn, name='mainn'),
    path('', views.index, name='index'),  # Adding the index route here
    path('admin/', admin_view, name='admin_view'),  # Admin view route
    path('admin_login/', admin_login, name='admin_login'),  # Admin login route
    path('admin_page/', admin_page, name='admin_page'),  # Admin page route
    path('about/', views.about, name='about'),
]
