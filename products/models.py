from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name="users_product")

    product_name = models.CharField(max_length=250, blank=False)
    product_description = models.TextField(max_length=1000, blank=False)
    product_thumbnail = models.ImageField(upload_to='product_thumbnail', blank=False, null=False)

    def __str__(self):
        return self.product_name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images', blank=False, null=False)

    def __str__(self):
        return self.product.product_name
