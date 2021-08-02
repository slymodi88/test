from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from carts.api.serializers import CartSerializer
from carts.models import Cart


class CartApi(GenericViewSet):
    @action(methods=['get'], detail=False)
    def detail(self, request, *args, **kwargs):
        print('Cart')
        # user_id = 1
        # cart = Cart.objects.get_or_create(user_id=user_id, order=None)
        # cart_items = cart.cart_item.all()
        #
        # serializer = CartSerializer(data=cart)
        #
        # return Response({"result": serializer.data, "message": "Done", "status": True},
        #                 status=status.HTTP_200_OK)
        return None

    @action(methods=['post'], detail=False)
    def add_product(self, request):
        data = request.data
        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data, "message": "Done", "status": True},
                            status=status.HTTP_200_OK)
        return Response({"message": serializer.errors, "status": False}, status=status.HTTP_400_BAD_REQUEST)
