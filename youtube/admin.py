from django.contrib import admin

from youtube.models import Bloger, Category


class BlogerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'is_favorites', 'category', 'url') # какие колонки выводим
    list_per_page = 50  #  кол-во выводимых элементов на страницу
    # list_display_links = ['url', 'name']  # кликабельна становится данные колонки


admin.site.register(Bloger, BlogerAdmin)
admin.site.register(Category)
