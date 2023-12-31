from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import OnlineShop
from .forms import OnlineShopForm
from django.urls import reverse

def index(request):
    online_shops = OnlineShop.objects.all()
    context = {'online_shops': online_shops}
    return render(request, 'app_advertisement/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisement/top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = OnlineShopForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = OnlineShop(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = OnlineShopForm()
    context = {'form':form}
    return render(request, 'app_advertisement/advertisement-post.html', context)

def register(request):
    return render(request, 'app_auth/register.html')

def login(request):
    return render(request, 'app_auth/login.html')

def profile(request):
    return render(request, 'app_auth/profile.html') 

