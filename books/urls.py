from django.urls import path
from .views import (
BookListView,
BookDetailView,
add_review,
book_reviews,
)

urlpatterns = [
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),

    path("reviews/add/", add_review, name="add-review"),
    path("reviews/<int:book_id>/", book_reviews, name="book-reviews"),
]


