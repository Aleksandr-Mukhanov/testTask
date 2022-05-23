from django.db import models


# Create your models here.
class Blocks(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    videoURL = models.URLField(verbose_name='URL Видео', blank=True)
    sort = models.IntegerField(verbose_name='Сортировка', default=500, blank=True)
    qntView = models.IntegerField(verbose_name='Кол-во показов', default=0, blank=True)

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'

    def __str__(self):
        return self.name


class Pages(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    slag = models.CharField(verbose_name='Слаг', max_length=100, blank=True)
    sort = models.IntegerField(verbose_name='Сортировка', default=500, blank=True)
    blocks = models.ManyToManyField(Blocks, verbose_name='Блоки', blank=True)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.name
