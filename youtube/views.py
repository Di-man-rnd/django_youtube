from django.shortcuts import render, render_to_response

# Create your views here.
from youtube.models import Bloger


def all_bloger(request):
    bloger = Bloger.objects.all().order_by('name')
    return render_to_response(
        'bloger.html',
        {'blogers': bloger}
    )
