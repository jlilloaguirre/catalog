from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book

class BookViewTest(APITestCase):
    
    def test_response_is_correct(self):
        book = Book.objects.create(
            title="Demo",
            description="Description",
            author="Author"
        )
        
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        returned_book = body[0]
        assert returned_book["id"] == book.id
        assert returned_book["title"] == book.title
        assert returned_book["description"] == book.description
        assert returned_book["author"] == book.author

    def test_detail_endpoint_returns_book_by_id(self):
        book = Book.objects.create(
            title="Detail Demo",
            description="Detail Description",
            author="Detail Author"
        )

        url = reverse('api:book-detail', kwargs={'pk': book.pk})
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body["id"] == book.id
        assert body["title"] == book.title
        assert body["description"] == book.description
        assert body["author"] == book.author

    def test_detail_endpoint_returns_404_for_missing_book(self):
        url = reverse('api:book-detail', kwargs={'pk': 999999})
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_404_NOT_FOUND
    def test_delete_endpoint_removes_book(self):
        book = Book.objects.create(
            title="Delete Demo",
            description="Delete Description",
            author="Delete Author"
        )

        url = reverse("api:book-detail", kwargs={"pk": book.pk})
        response = self.client.delete(url, format="json")

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Book.objects.filter(pk=book.pk).exists() is False

    def test_delete_endpoint_returns_404_for_missing_book(self):
        url = reverse("api:book-detail", kwargs={"pk": 999999})
        response = self.client.delete(url, format="json")

        assert response.status_code == status.HTTP_404_NOT_FOUND


class HealthViewTest(APITestCase):
    
    def test_response_is_correct(self):
        url = reverse('api:health')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body['status'] == 'ok'