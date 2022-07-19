from pyexpat import model
from attr import field
from rest_framework import serializers
from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            'user',
            'id',
            'shop_name',
            'dícription',
            'email',
            'phone_number',
            'address'
        ]