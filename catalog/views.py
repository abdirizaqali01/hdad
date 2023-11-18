from django.shortcuts import render, redirect
import stripe


def landing_page(request):
    return render(request, 'landingPage.html')

def loader(request):
    return render(request, 'loader.html')

def shop(request):
    return render(request, "shop.html")