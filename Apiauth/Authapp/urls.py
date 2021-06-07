from django.db.models import base
from django.urls import path,include
from . import views 
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('',views.LoginUser,basename='login')


urlpatterns = [
    path('', views.Home, name='home'),
    path('login/',include(router.urls), name='login'),
    path('api/',views.ApiEg.as_view(),name='api'),

]