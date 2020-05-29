from django.shortcuts import render
from product.models import Products




def index(request):
    """A view displays the index page"""

    # To find the first three ordered by the lowest price: 
    Product = Products.objects.all()

    return render(request, "index.html", {"Product": Product})