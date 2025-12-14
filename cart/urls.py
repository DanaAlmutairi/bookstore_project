from django.urls import path
from .views import CartDetailView, CartAddItemView, CartRemoveItemView

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart-detail'), # GET /api/cart/
    path('add/', CartAddItemView.as_view(), name='cart-add-item'), # POST /api/cart/add/
    path('remove/<int:pk>/', CartRemoveItemView.as_view(), name='cart-remove-item'), # DELETE /api/cart/remove/1/
]