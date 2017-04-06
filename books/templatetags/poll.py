from django import template
from books.models import Book
register = template.Library()


# ==========================filter=========================================
def cut2(value, arg):
    return value.replace(arg, '')

register.filter('cut2', cut2)


@register.filter
def filter_custom(value):
    return value + '!!'

# ==============================tag=====================================


@register.simple_tag()
def my_tag(v):
    return '~' + v + '~'


# =============================inclusion tag======================================

@register.inclusion_tag('book_inclusion_tag.html', takes_context=True)
def jump_link(context, arg):
    return {
        'link': '---------------',
        'title': arg,
    }