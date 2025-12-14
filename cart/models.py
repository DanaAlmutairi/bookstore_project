from django.db import models

from django.conf import settings
from books.models import Book


class Cart(models.Model):
    user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='cart'
    )

def __str__(self):
    return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(
    Cart,
    on_delete=models.CASCADE,
    related_name='items'
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Meta:
    unique_together = ('cart', 'book')

def __str__(self):
    return f"{self.book.title} ({self.quantity})"
