from django.contrib import admin
from lesson import models


# Register your models here.
@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    filter_horizontal = ['words']  # меняем виджет при выборе слов


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # автоматическое заполнение слага