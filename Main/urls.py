from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home page'),
    path('events/', views.events, name='events page'),
    path('sell/', views.sell, name='sell page'),

    path('checkout/', views.checkout, name='checkout page'),
    path('login/', views.loginpage, name='login page'),
    path('register/', views.register, name='register page'),
    path('logout/', views.logoutUser, name="logout"),
    path('awareness/', views.awareness, name='awareness page'),
    path('aboutus/', views.aboutus, name='aboutus page'),
    path('ContactUs/', views.contactus, name='contact page'),


]
