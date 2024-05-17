from re import template
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# from .forms import ResetPasswordForms,NewPasswordForms


urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset_password_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('register/',views.register,name='register'),
    path('loggout/',views.loggout,name='loggout'),
    path('profile/',views.profile,name='profile'),
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
    path('get_cart_data/',views.get_cart_data,name='get_cart_data'),
    path('change_quan/',views.change_quan,name='change_quan'),
    path('checkOut/',views.checkOut,name='checkOut'),
    path('placeOrder/',views.placeOrder,name='placeOrder'),
    path('proceed-to-pay/',views.razorpaycheck),
    path('order/',views.order,name='order'),
    path('orderview/<str:t_no>',views.orderview,name='orderview'),
    path('delete_order/<str:t_no>/',views.deleteOrder,name='delete_order'),
]




# (template_name="food/reset_password_confirm.html", form_class=NewPasswordForms )
# (template_name="food/reset_password.html", form_class=ResetPasswordForms)
# (template_name="food/reset_password_done.html")
# (template_name="food/reset_password_complete.html")