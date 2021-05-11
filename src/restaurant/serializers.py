from rest_framework import serializers
from restaurant.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('title', 'slug', 'phone', 'email', 'min_serve_time', 'min_order_tk', 'service_charge', 'vat_tax', 'city', 'address', 'environment', 'map_embed_url', 'is_active', 'is_orderable', 'extra_info', 'food_items', 'created_by', 'updated_by',)
