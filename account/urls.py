from django.urls import path
from .views import *

urlpatterns = [
    path('', accountPage, name="accountIndex"),
    
    # Register/login pages
    path('account_register', accountRegister, name="accountRegister"),
    path('account_login', accountLogin, name="accountLogin"),
    # Register/login processing
    path('register', register, name="register"),
    path('logout', logoutView, name="logoutView"),
    path('login', loginView, name="loginView"),

    # Account settings

]
