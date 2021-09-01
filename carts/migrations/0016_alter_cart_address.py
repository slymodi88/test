# Generated by Django 3.2.5 on 2021-08-31 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_auto_20210822_1921'),
        ('carts', '0015_alter_cart_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='address',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='addresses.address'),
        ),
    ]
