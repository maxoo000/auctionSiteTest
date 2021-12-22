from django.shortcuts import render, HttpResponse

# Create your views here.
def single_product(request):
    return render(request, 'shop/single_item.html')

def dnstest(request):
    return HttpResponse("loaderio-e6e74a17eb7775e520cf348b517d3098")