# Generated by Django 3.2.5 on 2021-08-22 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_auto_20210822_1921'),
        ('orders', '0002_auto_20210822_1927'),
        ('carts', '0002_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='addresses.address'),
        ),
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_cart', to='orders.order'),
        ),
    ]
