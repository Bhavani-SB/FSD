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
    path('add_room/', views.add_room, name='add_room'),
   
    path('add_patient/', views.add_patient, name='add_patient'),
    path('view_reports/', views.view_reports, name='view_reports'),
    path('about/', views.about, name='about'),
    
]
