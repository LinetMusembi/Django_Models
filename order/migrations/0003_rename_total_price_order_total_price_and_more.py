# Generated by Django 4.2.3 on 2023-08-09 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_cart_order_customer_order_delivery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Total_price',
            new_name='total_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product_ID',
        ),
    ]
