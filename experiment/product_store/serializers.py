from rest_framework.serializers import ModelSerializer

from .models import Product, Manufacturer


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', )


class ProductListSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Product
        fields = '__all__'
