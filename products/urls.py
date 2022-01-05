from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path("/product1/", views.product1, name='product-details'),
    path("/product_create/", views.product_create),
    path("/product_list/", views.product_list),
]