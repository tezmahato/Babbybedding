# Generated by Django 5.0 on 2024-02-04 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_producct_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='producct_image',
            new_name='product_image',
        ),
    ]