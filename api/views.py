from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book

class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "status": "ok"
        })

health_view = HealthView.as_view()

#
# /api/books - All methods (GET, POST)
#
class BookView(APIView):
    """ List all books, or create a new book """
    
    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        
        serializer = BookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class BookDetailView(APIView):
    """ Retrieve a single book by its ID """

    def get(self, request, pk, *args, **kwargs):
        book = Book.objects.filter(pk=pk).first()
        if book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        return Response(serializer.data)
        
book_view = BookView.as_view()
book_detail_view = BookDetailView.as_view()