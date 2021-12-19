from django.urls import path
from .views import *



urlpatterns = [
    path('asd', single_product, name="single_product"),
]
