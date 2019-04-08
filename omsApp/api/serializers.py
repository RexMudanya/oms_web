from rest_framework import serializers
from omsApp.models import Product, ProductType


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'pk', 'productType', 'name', 'price', 'image',
        ]
        read_only_fields = ['user']

    def validate_name(self, value):
        qs = Product.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This Product name already exists")
        return value


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = [
            'pk', 'type', 'description'
        ]

    def validate_type(self, value):
        qs = ProductType.objects.filter(type__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This Product Type already exists")
        return value

