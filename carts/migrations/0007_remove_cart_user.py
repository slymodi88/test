# Generated by Django 3.2.5 on 2021-08-25 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]
