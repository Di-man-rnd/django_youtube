from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from django.views.generic import CreateView, UpdateView, DeleteView
from youtube.form import *
from youtube.models import Bloger, Category

# ============= Function =============


def all_bloger(request):
    bloger = Bloger.objects.all().order_by('name')
    return render_to_response('bloger.html', {'blogers': bloger})


def detail_bloger(request, id):
    bloger = Bloger.objects.get(pk=id)
    similar = Bloger.objects.filter(category__id=bloger.category.id).exclude(pk=id)[:5]
    return render(request, 'detail.html', {'bloger': bloger, 'similar': similar})


def set_cat(request):
    bloger = Bloger.objects.get(pk=request.GET['pk'])
    bloger.category_id = int(request.GET['cat'])
    bloger.save()
    return HttpResponse('ok')


# =============== Class ===============


class BlogerList(ListView):
    model = Bloger
    # template_name = 'youtube/bloger_list.html'  # можем явно указать
    #       youtube - имя приложения
    #       bloger_list.html - название класса модели в нижнем регистре, через
    #                          нижнее подчеркивание и первое слово от (ListView):

    #  object_list - доступна в шаблоне  {% for publisher in object_list %} или
    #  bloger_list - доступна в шаблоне  по названию класса {% for publisher in bloger_list %} или
    #  context_object_name = my_blogers - задать в ручную, доступна в шаблоне  {% for publisher in my_blogers %}


class BlogerDetail(DetailView):
    model = Bloger # или явно указать запрос queryset = Publisher.objects.all(), а поле model убрать

    def get_context_data(self, **kwargs):
        context = super(BlogerDetail, self).get_context_data(**kwargs)
        context.update({'na': 'Dima'})
        context['year'] = '2017'
        return context

    # object - доступна в шаблоне  {% for publisher in object.url %}
    # то что подкинули в get_context_data доступна по имени {{ na }}

    # get_object– это метод, который получает и возвращает “рабочий” объект
    def get_object(self):
        obj = super(BlogerDetail, self).get_object()
        # obj.name = str(obj.name) + '-------'
        # obj.save()
        return obj




class CategoryList(ListView):
    model = Category


# отображает блогеров по конкретной категории
class CategoryDetailList(ListView):
    # model = Category
    template_name = 'youtube/category_detail.html'
    context_object_name = 'cat_detail'

    # динамически формируем запрос
    def get_queryset(self):
        self.cat = get_object_or_404(Category, pk=self.args[0])
        return Bloger.objects.filter(category__id=self.cat.id)

    # подкидываем данные
    def get_context_data(self, **kwargs):
        context = super(CategoryDetailList, self).get_context_data(**kwargs)
        context['cat'] = self.cat
        return context


def categoryAdd(request):
    if request.method == 'POST':
        form = categoryAddForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.data['name'])
            return HttpResponseRedirect('/bloger/category/add/')
    else:
        form = categoryAddForm()

    return render(request, 'youtube/category/add_function.html', {'form': form})


class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'youtube/category/add.html'


class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'youtube/category/update.html'
    template_name_suffix = '_update_form'


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')
    template_name = 'youtube/category/delete.html'


# ===========Helper ======================
class About(TemplateView):
    template_name = 'helper/about.html'
