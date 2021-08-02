# Generated by Django 3.2.5 on 2021-08-01 23:32

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('address_info', models.TextField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('total_cart', models.DecimalField(decimal_places=2, max_digits=20)),
                ('grand_total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('delivery_date', models.DateField()),
                ('shipping_fee', models.DecimalField(decimal_places=2, max_digits=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
