from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('checkout', views.checkout, name='checkout'),
    path('product', views.product, name='product')

]