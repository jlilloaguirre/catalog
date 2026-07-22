from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    new_field_1 = models.CharField(max_length=255, blank=True)
    new_field_2 = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

