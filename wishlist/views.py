from django.shortcuts import render, get_object_or_404, redirect 
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Wish_list
from products.models import Product



def add_product_to_wishlist(request, pk):
    """ 
    adds a product to the wish list using the product
    pk.
    
    """
    
    product = get_object_or_404(Product, id=pk) 
    
    wished_product = Wish_list.objects.get_or_create(wished_product=product,
                                                                    pk=pk, user=request.user)
    
    messages.info(request, 'The Product has been added')
    
    return render("wish_list.html", {'wished_product':wished_product})
    
    
      
    
    
        
    
    
    
def delete_product_from_wishlist(request, pk):
    """ 
    deletes a product from the wish list using the product
    pk.
    
    """


def see_wishlist(request, pk):
    """
    renders the wishlist to the users profile.html
    
    """
    wished_products = Wish_list.objects.filter(date_added__lte=timezone.now
    ().order_by('-date_added'))
    if wished_products is None:
        messages.error(request, 'You have no wishes...Please add some')
    else:
        return (render, 'profile.html', {'product': wished_products})
    