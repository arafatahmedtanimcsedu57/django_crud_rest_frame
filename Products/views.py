from django.shortcuts import render
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

# Create your views here.


class ProductsView(APIView):

    def get(self, request):
        products = Product.objects.all()
        productSerializer = ProductSerializer(products, many=True)
        return Response(productSerializer.data)

    def post(self, request):
        product = request.data
        productSerializer = ProductSerializer(data=product)

        if productSerializer.is_valid():
            productSerializer.save()
            return Response(productSerializer.data)
        return Response(productSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, id):
        product = self.get_object(id)
        productSerializer = ProductSerializer(product)
        return Response(productSerializer.data)

    def put(self, request, id):
        product = self.get_object(id)
        productSerializer = ProductSerializer(product, data=request.data)
        if productSerializer.is_valid():
            productSerializer.save()
            return Response(productSerializer.data)
        return Response(productSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
