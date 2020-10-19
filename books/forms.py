from django import forms
from django.conf.global_settings import LANGUAGES
import datetime
from django.core.exceptions import ValidationError

LANGUAGES_EMPTY = [('', 'wybierz język')] + LANGUAGES


def validate_year(value):
    year = value
    this_year = datetime.datetime.now().year
    if 0 > year >= this_year + 1:
        print('działa')
        raise ValidationError(f"Rok powinien się zawierać w przedziale 0 - {this_year}")


class SearchBookForm(forms.Form):
    title = forms.CharField(max_length=128, label='Tytuł', required=False)
    author = forms.CharField(max_length=128, label='Autor', required=False)
    language = forms.ChoiceField(choices=LANGUAGES_EMPTY, label='Język', required=False)
    published_date_from = forms.IntegerField(label='Data publikacji od', required=False, validators=[validate_year])
    published_date_to = forms.IntegerField(label='Data publikacji do', required=False, validators=[validate_year])