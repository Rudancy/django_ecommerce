from django.shortcuts import render
from products.models import Product
# Create your views here.


def carousel_products(request):
    products_carousel = Product.objects.all()
    return render(request, "products.html", {"products_carousel":products_carousel})