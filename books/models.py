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
    title = models.CharField(max_length=128, verbose_name='Tytuł')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Autor')
    published_date = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)],
                                         verbose_name='Data publikacji')
    isbn = models.CharField(max_length=13, null=True, blank=True, verbose_name='ISBN')
    page_count = models.IntegerField(verbose_name='Ilość stron')
    image_link = models.URLField(blank=True, null=True, verbose_name='Link do zdjęcia okładki')
    language = models.CharField(max_length=7, choices=LANGUAGES, blank=True, null=True, verbose_name='Język')

    def __str__(self):
        return self.title