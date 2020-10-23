from django.test import SimpleTestCase
from django.urls import reverse, resolve
from books.views import AddEditBookView, AllBooksView, ImportBookView, BookAPIView


class TestUrls(SimpleTestCase):

    def test_books_list_url_is_resoled(self):
        url = reverse('all_books')
        self.assertEqual(resolve(url).func.view_class, AllBooksView)

    def test_add_edit_book_url_is_resoled(self):
        url = reverse('add_book')
        self.assertEqual(resolve(url).func.view_class, AddEditBookView)

    def test_import_books_url_is_resoled(self):
        url = reverse('import_books')
        self.assertEqual(resolve(url).func.view_class, ImportBookView)

    def test_books_api_url_is_resoled(self):
        url = reverse('books_api')
        self.assertEqual(resolve(url).func.view_class, BookAPIView)