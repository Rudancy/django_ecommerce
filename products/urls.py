from django.conf.urls import url, include
from .views import all_products, product_information


urlpatterns=[
    url(r'^$', all_products, name='products'),
    url(r'^information/(?P<pk>\d+)$', product_information, name='product_information')
    ]