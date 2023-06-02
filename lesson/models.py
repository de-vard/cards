from django.db import models
from django.urls import reverse

from cards.models import Card
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Тег")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Lesson(models.Model):
    """Модель урока"""
    title = models.CharField(max_length=75, verbose_name='Название')
    words = models.ManyToManyField(Card, verbose_name='Слова')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата последнего редактирования', auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    tags = models.ForeignKey(Tag, on_delete=models.DO_NOTHING, blank=True, verbose_name='Теги')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('lesson:detail', args=[self.id])

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ['-created']
