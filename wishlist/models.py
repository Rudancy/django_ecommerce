from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.utils import timezone

class Wish_list(models.Model):
    wished_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)



    
    