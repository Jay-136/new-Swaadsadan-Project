from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('register/',views.register,name='register'),
    path('loggout/',views.loggout,name='loggout'),
    path('authentic/',views.authentic,name='authentic'),
    path('gujProductView/',views.gujProductView,name='gujProductView'),
    path('southProduct/',views.southProduct,name='southProduct'),
    path('punjabiProduct/',views.punjabiProduct,name='punjabiProduct'),
    path('rajsthaniProduct/',views.rajsthaniProduct,name='rajsthaniProduct'),
    path('indianStreetProduct/',views.indianStreetProduct,name='indianStreetProduct'),
    path('chinesseProduct/',views.chinesseProduct,name='chinesseProduct'),
    path('restaurantLogin/',views.restaurantLogin,name='restaurantLogin'),
    path('restaurantReg/',views.restaurantReg,name='restaurantReg'),
    path('cartView/',views.cartView,name='cartView'),

]




