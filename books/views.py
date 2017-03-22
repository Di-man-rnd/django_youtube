from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.mail import send_mail
from django.views import generic

from books.forms import ContactForm
from books.models import Book, Autor, Publisher
import time


#  время загрузки страницы  with Profiler() as p:
class Profiler(object):

    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))


def getbooks(request):
    with Profiler() as p:
        all_books = Book.objects.all()
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
        if request.POST.get('email', '') and '@' not in request.POST['email']:
            errors.append('Введите правильный адрес e-mail.')
        if not errors:
            # send_mail(
            #     request.POST['subject'],
            #     request.POST['message'],
            #     request.POST.get('e-mail', 'noreply@example.com'),
            #     ['siteowner@example.com'],
            # )
            print(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
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
            cd = form.cleaned_data # получаем словарь
            print(cd)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm({'subject': 'you are welcome!'})
    return render_to_response('books/contactform.html', {'form': form})


def thanks(request):
    return render_to_response('books/thanks.html')

# =============================================================================
# =============================================================================
# =============================================================================


class IndexView(generic.ListView):
    template_name = 'books/books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()
