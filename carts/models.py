from decimal import Decimal

from django.db import models
from django.db.models import Sum, F

from helpers.models import Timestamps


# from utils.utils import get_total_cart


class Cart(Timestamps):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_cart")
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE, related_name="order_cart", null=True,
                              blank=True)
    # address = models.ForeignKey("locations.Location", on_delete=models.CASCADE,d)

    def __str__(self):
        return str(self.user)

    @property
    def cart_total(self):
        return self.cart_item.aggregate(
            total_price=Sum(F('quantity') * F('item__price'))
        )["total_price"] or Decimal(0)

    @property
    def grand_total(self):
        return Decimal(self.cart_total + self.shipping_fee)

    @property
    def shipping_fee(self):
        if self.cart_total > 100:
            return Decimal(0)
        return Decimal(20)


class CartItem(Timestamps):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, related_name='cart_item')
    item = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    @property
    def items_total(self):
        return Decimal(self.item.price * self.quantity)

    def __str__(self):
        return str(self.cart)

# @receiver(post_save, sender=CartItem)
# def update_cart(sender, instance, **kwargs):
#     instance.cart.total_cart = get_total_cart(instance.cart)
#     instance.cart.save()
