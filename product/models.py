from django.db import models

# Create your models here.
class Product(models.Model):
    product_title=models.CharField(max_length=100)
    product_description=models.TextField()
    product_price=models.CharField(max_length=50)
    product_image=models.ImageField(upload_to="products/")