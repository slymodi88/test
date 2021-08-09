from rest_framework import serializers

from carts.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    updated_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    name = serializers.CharField(source='item.title')
    image = serializers.SerializerMethodField()
    description = serializers.CharField(source='item.description')
    items_total = serializers.SerializerMethodField()

    def get_image(self, CartItem):
        request = self.context.get('request')
        print(request)
        photo_url = CartItem.item.image.url
        return request.build_absolute_uri(photo_url)

    def get_items_total(self, instance):
        return "{} SAR".format(instance.items_total)

    def to_internal_value(self, data):
        data['cart'] = self.context.get('cart')
        return data

    class Meta:
        model = CartItem
        fields = "__all__"

    def create(self, validated_data):
        cart = validated_data.get('cart')
        item = validated_data.get('item_id')
        updated_quantity = validated_data.get('quantity')
        cart_item_exist = CartItem.objects.filter(cart_id=cart.id, item_id=item).exists()
        if cart_item_exist is False:
            cart_item = CartItem.objects.create(cart_id=cart.id, item_id=item, quantity=updated_quantity)
        else:
            cart_item = CartItem.objects.get(cart_id=cart.id, item_id=item)
            cart_item.quantity = updated_quantity
            cart_item.save()
        return cart_item


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(source='cart_item', many=True)
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    updated_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    cart_total = serializers.SerializerMethodField()
    shipping_fee = serializers.SerializerMethodField()
    grand_total = serializers.SerializerMethodField()

    def get_cart_total(self, instance):
        print(instance)
        return "{} SAR".format(instance.cart_total)

    def get_shipping_fee(self, instance):
        print(instance)
        return "{} SAR".format(instance.shipping_fee)

    def get_grand_total(self, instance):
        print(instance)
        return "{} SAR".format(instance.grand_total)

    class Meta:
        model = Cart
        fields = "__all__"
