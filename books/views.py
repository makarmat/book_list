import requests
from django.shortcuts import render, redirect
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from books.forms import SearchBookForm, AddEditBookForm, ImportBookForm
from books.serializers import BookSerializer
from books.models import Book
from django.views import View


# Create your views here.


class AllBooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by('-id')
        form = SearchBookForm()
        return render(request, 'all_books.html', {
            'books': books,
            'form': form
        })

    def post(self, request):
        if request.POST['action'] == 'search':
            form = SearchBookForm(request.POST)
            books = Book.objects.all().order_by('-id')
            if form.is_valid():
                title = form.cleaned_data['title']
                author = form.cleaned_data['author']
                language = form.cleaned_data['language']
                published_date_from = form.cleaned_data['published_date_from']
                published_date_to = form.cleaned_data['published_date_to']

                if title:
                    books = books.filter(title__icontains=title)
                if author:
                    books = books.filter(author__icontains=author)
                if language:
                    books = books.filter(language__icontains=language)
                if published_date_from:
                    books = books.filter(published_date__gte=published_date_from)
                if published_date_to:
                    books = books.filter(published_date__lte=published_date_to)
                form = SearchBookForm()
            return render(request, 'all_books.html', {
                'books': books,
                'form': form
            })

        if request.POST['action'] == 'del':
            book_id = request.POST['book_id']
            book = Book.objects.get(pk=book_id)
            book.delete()
            return redirect('all_books')

        if request.POST['action'] == 'edit':
            book_id = request.POST['book_id']
            book = Book.objects.get(pk=book_id)
            form = AddEditBookForm(instance=book)
            return render(request, 'add_edit_book.html', {
                'form': form,
                'book': book
            })


class AddEditBookView(View):
    def get(self, request):
        form = AddEditBookForm()
        return render(request, 'add_edit_book.html', {'form': form})

    def post(self, request):
        if request.POST['action'] == 'add':
            form = AddEditBookForm(request.POST)
            if form.is_valid():
                book = form.save(commit=False)
                isbn = form.cleaned_data['isbn']
                print(isbn)
                if '-' in isbn:
                    split_isbn = isbn.split('-')
                    clear_isbn = ''.join(split_isbn)
                    book.isbn = clear_isbn
                    print(clear_isbn)
                book.save()
                return redirect('all_books')
            return render(request, 'add_edit_book.html', {'form': form})

        if request.POST['action'] == 'edit':
            form = AddEditBookForm(request.POST)
            if form.is_valid():
                book_id = request.POST['book_id']
                book = Book.objects.get(pk=book_id)
                form = AddEditBookForm(request.POST, instance=book)
                book = form.save(commit=False)
                isbn = form.cleaned_data['isbn']
                print(isbn)
                if '-' in isbn:
                    split_isbn = isbn.split('-')
                    clear_isbn = ''.join(split_isbn)
                    book.isbn = clear_isbn
                    print(clear_isbn)
                book.save()
                return redirect('all_books')
            return render(request, 'add_edit_book.html', {'form': form})


class ImportBookView(View):
    def get(self, request):
        form = ImportBookForm()
        return render(request, 'import_books.html', {'form': form})

    def post(self, request):
        form = ImportBookForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            req_url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit' + '+intitle:' + '"' + keyword + '"'
            books_request = requests.get(url=req_url)
            books_json = books_request.json()
            books = books_json['items']

            for book in books:
                isbn = book['volumeInfo']['industryIdentifiers'][0]['identifier']
                if book['volumeInfo']['industryIdentifiers'][0]['type'] == 'OTHER':
                    isbn = None

                published_date = book['volumeInfo']['publishedDate']
                if '-' in published_date:
                    pd = published_date.split('-')
                    published_date = pd[0]

                if 'imageLinks' in book['volumeInfo']:
                    image_link = book['volumeInfo']['imageLinks']['thumbnail']
                else:
                    image_link = None

                Book.objects.get_or_create(
                    title=book['volumeInfo']['title'],
                    author=book['volumeInfo']['authors'][0],
                    published_date=published_date,
                    isbn=isbn,
                    page_count=book['volumeInfo']['pageCount'],
                    image_link=image_link,
                    language=book['volumeInfo']['language']
                )
            return redirect('all_books')
        return render(request, 'import_books.html', {'form': form})


class BookAPIView(generics.ListCreateAPIView):
    search_fields = ['title', 'author', 'language', 'published_date']
    filter_backends = (filters.SearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
