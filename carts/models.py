from django.db import models

from helpers.models import Timestamps


class Cart(Timestamps):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_cart")
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE, related_name="order_cart")
    shipping_fee = models.DecimalField(max_digits=20, decimal_places=2, default=20)
    total_cart = models.DecimalField(max_digits=20, decimal_places=2, default=0)


class CartItem(Timestamps):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, related_name='cart_item')
    item = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
