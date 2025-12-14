from rest_framework import serializers
from .models import Cart, CartItem
from books.serializers import BookSerializer
from books.models import Book


class CartItemSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        source='book',
        write_only=True
    )   

    class Meta:
        model = CartItem
        fields = ['id', 'book', 'book_id', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']