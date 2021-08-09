from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from carts.api.serializers import CartSerializer, CartItemSerializer
from carts.models import Cart, CartItem


class CartApi(GenericViewSet):
    permission_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=False)
    def details(self, request, *args, **kwargs):
        user_id = request.user.id
        cart, created = Cart.objects.get_or_create(user_id=user_id, order=None)
        serializer = CartSerializer(cart)
        return Response({"result": serializer.data, "message": "Done", "status": True},
                        status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def add_product(self, request):
        user_id = request.user.id
        data = request.data
        cart, created = Cart.objects.get_or_create(user_id=user_id, order=None)
        serializer = CartItemSerializer(data=data, context={'cart': cart, 'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data, "message": "Done", "status": True},
                            status=status.HTTP_200_OK)
        return Response({"result": serializer.errors, "message": "Done", "status": False},
                        status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=False)
    def remove_item(self, request):
        user_id = request.user.id
        data = request.data
        cart = Cart.objects.get(user_id=user_id, order=None)
        item = CartItem.objects.filter(cart=cart, item_id=data['item_id'])
        item.delete()
        return Response({"message": "Done", "status": True}, status=status.HTTP_200_OK)
