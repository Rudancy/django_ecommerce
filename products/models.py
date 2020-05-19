from django.db import models


#https://www.youtube.com/watch?v=Xjty8q524Jo&list=PLLRM7ROnmA9F2vBXypzzplFjcHUaKWWP5&index=2

BRAND_CHOICES = (
    ('AD', 'Addidas'),
    ('NK', 'Nike'),
    ('CV', 'Coverse'),
    ('DD', 'Diadora'),
    ('EA', 'Emporium Armani'),
    ('NB', 'New Balance'),
    ('PM', 'Puma'),
    
)

AGE_CHOICES = (
    ('M', 'Mens'),
    ('F', 'Women'),
    ('k', 'kIDS')
    )


class Product(models.Model):
    name = models.CharField(max_length=200, default='')
    description=models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    image_1 = models.ImageField(upload_to='images')
    image_2 = models.ImageField(upload_to='images')
    year_created = models.DateField(auto_now=False)
    history_of_product = models.TextField()
    brand = models.CharField(max_length=2, choices=BRAND_CHOICES, default='')
    age = models.CharField(max_length=1, choices=AGE_CHOICES, default='')
    
    
    def __str__(self):
        return self.name
    

# Create your models here.
