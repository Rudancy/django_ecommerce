from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Wish_list
from products.models import Product
from django.contrib.auth.decorators import login_required




def add_product_to_wishlist(request, pk):
    """ 
    adds a product to the wish list using the product
    pk.
    
    """
     #product = get_object_or_404(Product, id=pk) 
    
    #wished_product = Wish_list.objects.get_or_create(wished_product=product,
    #                                                pk=pk, user=request.user)
    products = Product.objects.filter(wish_list__user=request.user)
    
    
    page = products.page(1)
    my_products = page.object_list
    
    
    
    
    
    
    messages.info(request, 'The Product has been added')
    print(products) 
    #return render(request, "wish_list.html", {'products':products, 'my_products':my_products})


def see_wishlist(request, pk):
    """
    renders the wishlist to the users profile.html
    
    """
    user = get_object_or_404(User, id=pk)
    
    wished_products = Wish_list.objects.get(id=1)
    
    if wished_products is None:
        messages.error(request, 'You have no wishes...Please add some')
    else:
        return render(request, 'wish_list.html', {'wished_products': wished_products, 'user':user })

    
      
    
    
        
def delete_product_from_wishlist(request, pk):
    """ 
    deletes a product from the wish list using the product
    pk.
    
    """



