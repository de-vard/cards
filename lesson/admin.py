from django.contrib import admin
from lesson import models


# Register your models here.
@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    filter_horizontal = ['redy_words']  # меняем виджет при выборе слов


