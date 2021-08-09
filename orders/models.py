import datetime
from django.utils import timezone
from django.contrib.gis.db import models

from helpers.models import Timestamps


class Order(Timestamps):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user_order')
    order_total = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    grand_total = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True, default=timezone.now)
    shipping_fee = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    # address = models.ForeignKey("locations.Location", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.id)


class OrderProduct(Timestamps):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    item = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_item')
    quantity = models.FloatField()
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return str(self.id)
