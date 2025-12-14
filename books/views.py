from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

from .models import Book
from .serializers import BookSerializer

# Mongo helpers
from .mongo_reviews import add_review as mongo_add_review
from .mongo_reviews import get_reviews as mongo_get_reviews


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "author", "isbn"]


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_review(request):
    """
    POST /api/books/reviews/add/
    Body: { "book_id": 1, "rating": 5, "comment": "Nice" }
    Requires JWT (Authorization: Bearer <token>)
    """
    book_id = request.data.get("book_id")
    rating = request.data.get("rating")
    comment = request.data.get("comment", "")

    if not book_id or rating is None:
        return Response(
            {"error": "book_id and rating are required."},
            status=status.HTTP_400_BAD_REQUEST
    )

    # store username/email as string in Mongo
    user_str = request.user.username or request.user.email or str(request.user)

    try:
        doc = mongo_add_review(book_id, user_str, rating, comment)
        return Response(doc, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["GET"])
@permission_classes([AllowAny])
def book_reviews(request, book_id):
    """
    GET /api/books/<book_id>/reviews/
    Public endpoint (no auth needed)
    """
    try:
        reviews = mongo_get_reviews(book_id)
        return Response(reviews, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )