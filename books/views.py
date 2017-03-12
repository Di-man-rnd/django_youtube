from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from books.models import Book, Autor, Publisher


def getbooks(request):
    all_books = Book.objects.all();
    return render_to_response('books/books.html', {'books': all_books})


def search(request):
    er = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            er.append('Введите поисковый запрос')
        elif len(q) > 20:
            er.append('Запрос должен быть менее 20 символов')
        else:
            books = Book.objects.filter(title__contains=request.GET['q'])
            return render_to_response('books/search_result.html', {'books': books, 'q': request.GET['q']})
    return render_to_response('books/search_form.html', {'er': er})
