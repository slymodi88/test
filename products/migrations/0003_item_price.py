# Generated by Django 3.2.5 on 2021-08-22 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
        ),
    ]