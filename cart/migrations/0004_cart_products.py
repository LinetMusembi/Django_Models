# Generated by Django 4.2.3 on 2023-08-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_product_description_alter_product_image'),
        ('cart', '0003_alter_cart_list_of_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='inventory.product'),
        ),
    ]
