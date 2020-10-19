from django.shortcuts import render, redirect, get_object_or_404

from books.forms import SearchBookForm
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
        form = SearchBookForm(request.POST)
        books = Book.objects.all().order_by('title')
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            language = form.cleaned_data['language']
            published_date_from = form.cleaned_data['published_date_from']
            published_date_to = form.cleaned_data['published_date_to']

            if title:
                books = Book.objects.filter(title__icontains=title)
            if author:
                books = Book.objects.filter(author__icontains=author)
            if language:
                books = Book.objects.filter(language__icontains=language)
            if published_date_from:
                books = Book.objects.filter(published_date__gte=published_date_from)
            if published_date_to:
                books = Book.objects.filter(published_date__lte=published_date_to)
            form = SearchBookForm()
        return render(request, 'all_books.html', {
            'books': books,
            'form': form
        })
