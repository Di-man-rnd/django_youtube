from django.shortcuts import render, render_to_response
from books.models import Book, Autor, Publisher


def getbooks(request):
    all_books = Book.objects.all();
    return render_to_response('books/books.html', {'books': all_books})
