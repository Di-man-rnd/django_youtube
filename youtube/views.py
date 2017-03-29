from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from wheel.metadata import pkginfo_to_dict

from youtube.models import Bloger


def all_bloger(request):
    bloger = Bloger.objects.all().order_by('name')
    return render_to_response(
        'bloger.html',
        {'blogers': bloger}
    )


def detail_bloger(request, id):
    bloger = Bloger.objects.get(pk=id)
    similar = Bloger.objects.filter(category__id=bloger.category.id).exclude(pk=id)[:5]
    return render(request, 'detail.html', {'bloger': bloger, 'similar': similar})


def set_cat(request):
    bloger = Bloger.objects.get(pk=request.GET['pk'])
    bloger.category_id = int(request.GET['cat'])
    bloger.save()
    return HttpResponse('ok')
