from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def all_products(request):
    """
    a view that allows the customer to 
    see all products and paginates them
    """
    
    
    products = Product.objects.all()
    
    
    page =request.GET.get('page', 1)
    
    paginator= Paginator(products, 8)
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products":products})
    


def product_information(request, pk):
    """
    creates a view that returns information about 
    a specified product
    
    """
    
    product_information = get_object_or_404 (Product, pk=pk)
    return render(request, "product_information.html", {"product_information": product_information})
    
    

def brand_products(request, BRAND_CHOICES):
    """
    a view that returns all the products within a 
    certain brand
    """
    BRAND_CHOICES = Product.objects.filter(brand=BRAND_CHOICES)
    return render(request, "brand_products.html", {"product_brand":BRAND_CHOICES})
    
    

def age_products(request, AGE_CHOICES):
    """
    a view to show the male and female, kids
    sections
    """
    AGE_CHOICES = Product.objects.filter(age=AGE_CHOICES)
    return render(request, "age_products.html", {"age_products":AGE_CHOICES})