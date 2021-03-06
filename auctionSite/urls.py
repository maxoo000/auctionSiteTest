"""auctionSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views
from auction.views import dnstest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('account/', include('account.urls'), name='account'),
    path('auction/', include('auction.urls'), name='auction'),
    path('products/', include('products.urls'), name='products'),
    path('payment/', include('payment.urls'), name='payment'),
    path('loaderio-e6e74a17eb7775e520cf348b517d3098/', dnstest, name='payment'),
]
