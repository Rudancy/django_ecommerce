from django.conf.urls import url, include
from .views import all_products, product_information, brand_products, age_products


urlpatterns=[
    url(r'^$', all_products, name='products'),
    url(r'^information/(?P<id>\d+)', product_information, name='product_information'),
    url(r'^age/(?P<AGE_CHOICES>\w+)', age_products, name='age_products'),
    url(r'^brand/(?P<BRAND_CHOICES>\w+)', brand_products, name='brand_products'),
    ]