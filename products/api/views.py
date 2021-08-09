from django.db.models import Min, F
from django_filters.rest_framework import backends
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from branches.models import City, BranchItem
from mixins.paginator import CustomPagination
from products.models import Product
from products.api.serializers import ProductSerializer, BranchItemSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = (backends.DjangoFilterBackend, SearchFilter)
    # filter_fields = ['isavailable', 'created_at', 'categories__title']
    # search_fields = ['title', 'categories__title']
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        user = request.user.id
        city = City.objects.get(user=user)
        qs = BranchItem.objects.filter(branch__cities=city.id, item__isavailable=True)
        print(qs)
        queryset = self.paginate_queryset(self.filter_queryset(qs))
        serializer = BranchItemSerializer(queryset, many=True)
        return self.paginator.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data, "message": "Done", "status": True},
                            status=status.HTTP_201_CREATED)
        return Response({"message": serializer.errors, "status": False}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs["pk"])
        serializer = ProductSerializer(product)
        return Response({"result": serializer.data, "message": "Done", "status": True}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        data = request.data
        product = get_object_or_404(Product, id=kwargs["pk"])
        serializer = ProductSerializer(instance=product, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data, "message": "Done", "status": True}, status=status.HTTP_200_OK)
        return Response({"message": serializer.errors, "status": False}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs["pk"])
        product.delete()
        return Response({"message": "Done", "status": True}, status=status.HTTP_200_OK)
