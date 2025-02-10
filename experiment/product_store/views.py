import django_filters.rest_framework
from django.shortcuts import render
from rest_framework import generics

from .filters import ProductFilter
from .models import Product
from .serializers import ProductListSerializer


# Create your views here.
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = ProductFilter
