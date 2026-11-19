from django.db import models

BOOK_STATUS_CHOICES = (
    ("to_read", "To Read"),
    ("reading", "Reading"),
    ("read", "Read"),
)


class Book (models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=BOOK_STATUS_CHOICES)
    rating = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

