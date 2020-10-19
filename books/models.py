from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=64)


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
    isbn = models.CharField(max_length=13)
    page_count = models.IntegerField([MinValueValidator(0)])
    image_link = models.URLField()