from django.urls import path
from ap1 import views

urlpatterns = [
    path("/k1/", views.k1),
    path("/k2/", views.k2),
    path("/k3/", views.k3),
]