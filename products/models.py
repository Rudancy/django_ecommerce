from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, default='')
    description=models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    year_created = models.DateField(auto_now=False)
    history_of_product = models.TextField()
    
    def __str__(self):
        return self.name
    

# Create your models here.
