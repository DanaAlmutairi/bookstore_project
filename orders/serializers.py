from rest_framework import serializers
from .models import Order, OrderItem
from books.serializers import BookSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'book', 'quantity', 'price_at_purchase']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'status', 'total_price', 'created_at', 'items']
        read_only_fields = ['status', 'total_price', 'created_at', 'items']