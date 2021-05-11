from rest_framework import serializers
from order.models import Cart, Order, Discount


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ('updated_at', 'deleted_at', 'created_by', 'updated_by')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('updated_at', 'deleted_at', 'created_by', 'updated_by')


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'
