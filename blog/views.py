from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from youtube.models import Bloger, Category
from .tasks import just_print


class IndexPage(TemplateView):
    template_name = 'index.html'


class ListPage(ListView):
    # model = Bloger
    # queryset = Bloger.objects.all()[:5]
    template_name = 'list.html'
    paginate_by = 2

    # подкинуть данные в шаблон
    def get_context_data(self, **kwargs):
        context = super(ListPage, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

    # выборка данных
    def get_queryset(self):
        if self.param:
            content = Bloger.objects.filter(category=self.param)
        else:
            content = Bloger.objects.all()[:4]
        return content

    # получение параметров GET, POST запроса
    def get(self, request, *args, **kwargs):
        try:
            self.param = args[0]
        except IndexError:
            self.param = None
        return super(ListPage, self).get(request, *args, **kwargs)

    # конструктор в данном случае он тут не нужен
    def __init__(self):
        return super(ListPage, self).__init__()


class DetailPage(DetailView):
    model = Bloger
    template_name = 'detail_page.html'

    def get_context_data(self, **kwargs):
        just_print.delay()
        return super(DetailPage, self).get_context_data(**kwargs)
