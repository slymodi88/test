# Generated by Django 3.2.5 on 2021-08-02 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_alter_cartitem_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='shipping_fee',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=20),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_cart',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
