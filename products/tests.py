from django.test import TestCase
from .models import Product
# Create your tests here.

###########product tests#############

class ProductTests(TestCase):
    """ 
    run tests against our product
    models
    
    """
    
    
    def test_str(self):
        test_name = Product(name='A Product')
        self. assertEqual(str(test_name), 'A Product')
    