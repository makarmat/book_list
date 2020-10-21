from django.shortcuts import render, redirect
from books.forms import SearchBookForm, AddEditBookForm
from books.models import Book
from django.views import View


# Create your views here.


class AllBooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by('title')
        form = SearchBookForm()
        return render(request, 'all_books.html', {
            'books': books,
            'form': form
        })

    def post(self, request):
        if request.POST['action'] == 'search':
            form = SearchBookForm(request.POST)
            books = Book.objects.all().order_by('title')
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