from django.contrib import admin

# Register your models here.
from product.models import Product


class product_admin(admin.ModelAdmin):
    list_display=('product_title','product_description','product_price','product_image')

admin.site.register(Product,product_admin)