from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.mail import send_mail

from books.forms import ContactForm
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


def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Введите тему.')
        if not request.POST.get('message', ''):
            errors.append('Введите сообщение.')
        if request.POST.get('email', '') and '@' not in request.POST['e-mail']:
            errors.append('Введите правильный адрес e-mail.')
        if not errors:
            # send_mail(
            #     request.POST['subject'],
            #     request.POST['message'],
            #     request.POST.get('e-mail', 'noreply@example.com'),
            #     ['siteowner@example.com'],
            # )
            # return HttpResponseRedirect('/contact/thanks/')
            print(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
    return render_to_response('books/contact.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'mail': request.POST.get('email', ''),
    })


def contactform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('books/contactform.html', {'form': form,})


def thanks(request):
    return render_to_response('books/thanks.html')