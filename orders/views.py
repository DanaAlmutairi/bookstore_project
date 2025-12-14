from rest_framework import generics, permissions
from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.models import Cart

class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user

        # get user's cart
        cart = Cart.objects.get(user=user)

    # calculate total price
        total_price = sum(
            item.book.price * item.quantity
            for item in cart.items.all()
    )

    # create order with required fields
        order = serializer.save(
            user=user,
            total_price=total_price
        )

    # move cart items into order items
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                book=item.book,
                quantity=item.quantity,
                price_at_purchase=item.book.price
            )

    # clear cart
        cart.items.all().delete()
