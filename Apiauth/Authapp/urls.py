from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home, name='home'),
    path('login/', views.Loginuser, name='login')
]