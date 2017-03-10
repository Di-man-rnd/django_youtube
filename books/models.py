from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    website = models.URLField(blank=True)

    class Meta:
        db_table = 'publisher'

    def __str__(self):
        return self.name


class Autor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)

    class Meta:
        db_table = 'autor'
        ordering = ['last_name']
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return u'%s  %s (%s)' % (self.first_name, self.last_name, self.length())

    def length(self):
        return Book.objects.filter(autor=self.id).count()


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    publication_date = models.DateField(verbose_name='Дата публикации', null=True, blank=True)
    autor = models.ManyToManyField(Autor)
    publisher = models.ForeignKey(Publisher)

    class Meta:
        db_table = 'book'
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'
        ordering = ['-title']

    def __str__(self):
        return self.title
