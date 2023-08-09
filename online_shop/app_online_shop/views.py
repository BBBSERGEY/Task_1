from django.shortcuts import render
from django.http import HttpResponse
from .models import OnlineShop


def index(request):
    online_shops = OnlineShop.objects.all()
    context = {'online_shops': online_shops}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    return render(request, 'advertisement_post.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html') 