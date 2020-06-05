from django.shortcuts import render
from core.models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView

def home(request):
    context = {
        "items":Item.objects.all()
    }

    return render(request, 'home-page.html', context)

class HomeView(ListView):
    model = Item
    template_name = "home-page.html"
    context_object_name = 'items'

def checkout(request):
    return render(request, 'checkout-page.html')

def product(request):
    return render(request, 'product-page.html')        
