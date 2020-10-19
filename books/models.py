from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from languages.fields import LanguageField
from django.conf.global_settings import LANGUAGES


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=64)

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
    isbn = models.CharField(max_length=13, null=True, blank=True)
    page_count = models.IntegerField()
    image_link = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=7, choices=LANGUAGES, blank=True, null=True)

    def __str__(self):
        return self.title