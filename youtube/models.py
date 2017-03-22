from django.db import models


class Bloger(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=200)
    url = models.URLField(verbose_name=u'Ссылка')
    img = models.CharField(verbose_name=u'Аватарка', max_length=500)
    category = models.ForeignKey(verbose_name=u'Катагория')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name=u'Название')
    sort = models.SmallIntegerField(verbose_name=u'Сортировка', default=100)
    active = models.BooleanField(verbose_name=u'Активность', default=True)