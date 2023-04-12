from django.core import validators
from django.db import models
from django.conf import settings


class WrongCards(models.Model):
    """Карточки с ошибками"""
    CHOICE = ((None, 'Выберите в чем ошибка'), ('a', 'терминe'), ('b', 'определение'), ('c', 'произношение'))
    mistake_in = models.CharField('Ошибка в', choices=CHOICE, max_length=3, blank=True)
    card = models.ForeignKey('Card', on_delete=models.CASCADE,
                             verbose_name='Ошибка', blank=True, related_name='wrong_cards')
    error_text = models.TextField('Подробнее об ошибки', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               verbose_name='Автор', blank=True, )

    def __str__(self):
        return self.mistake_in


class Card(models.Model):
    """Карточки слов"""
    term = models.CharField('Термин', max_length=100)
    transcription = models.CharField('Транскрипция', max_length=100)
    definition = models.CharField('Определение', max_length=100)
    audi = models.FileField(upload_to='audi/%Y/%m/%d', verbose_name='Произношение',
                            validators=[validators.RegexValidator(regex=".mp3")], )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               verbose_name='Автор', blank=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата последнего редактирования', auto_now=True)

    def __str__(self):
        return f'{self.term} - {self.definition}'

    class Meta:
        verbose_name = "Карточку"
        verbose_name_plural = "Карточки"
        ordering = ['-created']
