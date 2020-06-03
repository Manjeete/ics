from django.shortcuts import render
from core.models import Item, OrderItem, Order

def home(request):
    context = {
        "items":Item.objects.all()
    }

    return render(request, 'home-page.html', context)


def checkout(request):
    return render(request, 'checkout-page.html')

def product(request):
    return render(request, 'product-page.html')        
