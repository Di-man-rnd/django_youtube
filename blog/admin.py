from django.contrib import admin
from blog.models import *


class MainInlines(admin.TabularInline):
    model = PhoneNotis
    extra = 2


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    inlines = [MainInlines]
