from django.contrib.gis.db import models

from helpers.models import Timestamps


class Order(Timestamps):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user_order')
    address_info = models.TextField()
    location = models.PointField()
    total_cart = models.DecimalField(max_digits=20, decimal_places=2)
    grand_total = models.DecimalField(max_digits=20, decimal_places=2)
    delivery_date = models.DateField()
    shipping_fee = models.DecimalField(max_digits=20, decimal_places=2)


class OrderProduct(Timestamps):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    item = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.FloatField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
