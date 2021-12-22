from django.shortcuts import render, HttpResponse
from django.utils import timezone


# Create your views here.
def index(request):
    a = timezone.now()
    return render(request, 'home/index.html', context={"time": a})
