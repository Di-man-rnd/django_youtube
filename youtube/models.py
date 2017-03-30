from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ModelForm, Textarea


class BlogerManager(models.Manager):

    def stok(self):
        return self.exclude(category__id=1)[:2]


class Bloger(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=200)
    url = models.URLField(verbose_name=u'Ссылка')
    img = models.FileField(verbose_name=u'Аватарка', upload_to='bloger/', blank=True, null=True)
    category = models.ForeignKey('Category', verbose_name=u'Катагория', default=1)
    is_favorites = models.BooleanField(verbose_name=u'Избранное', default=False, help_text=u'для избранного !')
    objects = BlogerManager()

    class Meta:
        verbose_name = 'Блогер'
        verbose_name_plural = 'Блогеры'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=200)
    sort = models.SmallIntegerField(verbose_name=u'Сортировка', default=100, blank=True, null=True)
    active = models.BooleanField(verbose_name=u'Активность', default=True)
    img = models.FileField(upload_to=u'category/', verbose_name=u'Картинка', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('category_detail', args=[self.pk])


# ====================== SIGNALS ======================
# bloger del img
from youtube.signals import bloger_del_img
