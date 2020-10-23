from django.test import TestCase, Client
from django.urls import reverse
from books.models import Book
from books.forms import SearchBookForm
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.all_books_url = reverse('all_books')
        self.add_edit_book_url = reverse('add_book')
        self.import_book_url = reverse('import_books')
        self.book1 = Book.objects.create(
            title='Test test',
            author='Jan Testowy',
            published_date='2005',
            isbn='9788301000001',
            page_count='250',
            language='pl'

        )

    def test_all_books_GET(self):
        response = self.client.get(self.all_books_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_books.html')

    def test_add_edit_book_GET(self):
        response = self.client.get(self.add_edit_book_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_edit_book.html')

    def test_import_book_GET(self):
        response = self.client.get(self.import_book_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'import_books.html')




