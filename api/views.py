from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "status": "ok"
        })

health_view = HealthView.as_view()

class BookView(APIView):
    """ List all books, or create a new book """
    
    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)
    

book_view = BookView.as_view()