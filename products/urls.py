from django.conf.urls import url, include
from .views import all_products, product_information, brand_products


urlpatterns=[
    url(r'^$', all_products, name='products'),
    url(r'^brand/(?P<BRAND_CHOICES>\w+)', brand_products, name='brand_products'), 
    url(r'^information/(?P<pk>\d+)$', product_information, name='product_information')
    ]