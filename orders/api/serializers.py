from django.core.mail import send_mail
from rest_framework import serializers

from carts.models import Cart, CartItem
from orders.models import OrderProduct, Order


class OrderCreateSerializer(serializers.ModelSerializer):
    order_total = serializers.SerializerMethodField()
    shipping_fee = serializers.SerializerMethodField()
    grand_total = serializers.SerializerMethodField()

    def get_order_total(self, instance):
        return "{} SAR".format(instance.order_total)

    def get_shipping_fee(self, instance):
        return "{} SAR".format(instance.shipping_fee)

    def get_grand_total(self, instance):
        return "{} SAR".format(instance.grand_total)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data.get('user')
        email = user.email
        cart = Cart.objects.get(user=user, order=None)
        order = Order.objects.create(user=user, order_total=cart.cart_total, grand_total=cart.grand_total,
                                     shipping_fee=cart.shipping_fee)
        cart.order = order
        items = CartItem.objects.filter(cart=cart)
        for i in items:
            OrderProduct.objects.create(order=order, item=i.item, quantity=i.quantity, price=i.item.price)
        cart.save()
        order.save()
        send_mail(
            'your order is ready',
            'thank you',
            'slymodi88@gmail.com',
            [email],
        )
        return order


class OrderSerializer(serializers.ModelSerializer):
    order_total = serializers.SerializerMethodField()
    shipping_fee = serializers.SerializerMethodField()
    grand_total = serializers.SerializerMethodField()

    def get_order_total(self, instance):
        return "{} SAR".format(instance.order_total)

    def get_shipping_fee(self, instance):
        return "{} SAR".format(instance.shipping_fee)

    def get_grand_total(self, instance):
        return "{} SAR".format(instance.grand_total)

    class Meta:
        model = Order
        fields = "__all__"
