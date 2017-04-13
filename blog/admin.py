from django.contrib import admin
from blog.models import *
from ckeditor.fields import RichTextField

class MainInlines(admin.TabularInline):
    model = PhoneNotis
    extra = 2


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    inlines = [MainInlines]

    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )
