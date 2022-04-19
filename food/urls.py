from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('register/',views.register,name='register'),
    path('loggout/',views.loggout,name='loggout'),
    path('authentic/',views.authentic,name='authentic'),
    path('authentic/<str:slug>',views.gujProductView,name='gujProductView'),
    path('authentic/<str:slug>',views.southProduct,name='southProduct'),
    path('authentic/<str:slug>/',views.punjabiProduct,name='punjabiProduct'),
    path('authentic/<str:slug>/',views.rajsthaniProduct,name='rajsthaniProduct'),
    path('authentic/<str:slug>/',views.indianStreetProduct,name='indianStreetProduct'),
    path('authentic/<str:slug>/',views.chinesseProduct,name='chinesseProduct'),
    path('restaurantLogin/',views.restaurantLogin,name='restaurantLogin'),
    path('restaurantReg/',views.restaurantReg,name='restaurantReg'),
    path('cartView/',views.cartView,name='cartView'),
    path('get_cart_data',views.get_cart_data,name='get_cart_data'),
    path('change_quan',views.change_quan,name='change_quan'),

]




