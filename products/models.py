from django.db import models
from django.urls import reverse

class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.TextField()
    summary     = models.TextField(default='this is cool')

def get_absolute_url(self):
    return reverse("products:product_details",kwargs={"id": self.id})#f"/products/{self.id}/"