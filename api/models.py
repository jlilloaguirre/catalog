from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    new_field_1 = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

