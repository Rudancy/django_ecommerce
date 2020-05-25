from django.conf.urls import url, include
from .views import add_product_to_wishlist, delete_product_from_wishlist, see_wishlist

urlpatterns=[
    url(r'^(?P<pk>\d+)$', see_wishlist , name='see_wishlist'),
    url(r'^add/(?P<pk>\d+)', add_product_to_wishlist, name='add_product_to_wishlist'),
    
    
    ]