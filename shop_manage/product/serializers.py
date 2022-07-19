from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'user',
            'shop',
            'id',
            'product_name',
            'description',
            'price',
            'create_date'
        ]