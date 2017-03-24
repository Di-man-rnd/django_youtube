from django.db import models


class Bloger(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=200)
    url = models.URLField(verbose_name=u'Ссылка')
    img = models.FileField(verbose_name=u'Аватарка', upload_to='bloger/', blank=True, null=True)
    category = models.ForeignKey('Category', verbose_name=u'Катагория', default=1)
    is_favorites= models.BooleanField(verbose_name=u'Избранное', default=False, help_text=u'для избранного !')

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