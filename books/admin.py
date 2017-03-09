from django.contrib import admin

from .models import Autor, Publisher, Book

# Register your models here.
admin.site.register(Autor)
admin.site.register(Book)
admin.site.register(Publisher)