from django import forms
from django.conf.global_settings import LANGUAGES
import datetime
import pyisbn
from django.core.exceptions import ValidationError
from books.models import Book

LANGUAGES_EMPTY = [('', 'wybierz język')] + LANGUAGES


def validate_year(year):
    this_year = datetime.datetime.now().year
    if year < 0:
        raise ValidationError('Rok publikacji nie może być mniejszy od zera!')
    elif year > this_year:
        raise ValidationError('Rok publikacji nie może być większy niż {}!'.format(this_year))


def validate_isbn(isbn):
    if not pyisbn.validate(isbn):
        raise ValidationError('Nieprawidłowy numer ISBN!')


class SearchBookForm(forms.Form):
    title = forms.CharField(max_length=128, label='Tytuł', required=False)
    author = forms.CharField(max_length=128, label='Autor', required=False)
    language = forms.ChoiceField(choices=LANGUAGES_EMPTY, label='Język', required=False)
    published_date_from = forms.IntegerField(label='Data publikacji od', required=False, validators=[validate_year])
    published_date_to = forms.IntegerField(label='Data publikacji do', required=False, validators=[validate_year])


class AddEditBookForm(forms.ModelForm):
    published_date = forms.IntegerField(label='Data publikacji', validators=[validate_year])
    isbn = forms.CharField(label='ISBN', validators=[validate_isbn])

    class Meta:
        model = Book
        fields = '__all__'


class SearchBookForm(forms.Form):
    keyword = forms.CharField(label='Słowo kluczowe API')