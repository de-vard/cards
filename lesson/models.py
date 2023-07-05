from django.db import models
from django.urls import reverse

from cards.models import Card
from courses.models import Course
from cards.models import Image


class Lesson(models.Model):
    """Модель урока"""
    title = models.CharField(max_length=75, verbose_name='Название')
    redy_words = models.ManyToManyField(Card, verbose_name='Слова')
    word_eng = models.CharField('Термин', max_length=75)
    word_rus = models.CharField('Определение', max_length=75)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курсы')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата последнего редактирования', auto_now=True)
    image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Фото'
    )

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('lesson:detail', args=[self.id])

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ['-created']
