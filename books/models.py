from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf.global_settings import LANGUAGES


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=128, verbose_name='Tytuł')
    author = models.CharField(max_length=128, verbose_name='Autor')
    published_date = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)],
                                         verbose_name='Data publikacji')
    isbn = models.CharField(max_length=18, null=True, blank=True, verbose_name='ISBN')
    page_count = models.IntegerField(verbose_name='Ilość stron')
    image_link = models.URLField(blank=True, null=True, verbose_name='Link do zdjęcia okładki')
    language = models.CharField(max_length=7, choices=LANGUAGES, blank=True, null=True, verbose_name='Język')

    def __str__(self):
        return self.title