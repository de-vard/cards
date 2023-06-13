from django.db.models import Count
from django.shortcuts import render

# TODO:Всуну пока сюда так как не знаю куда всунуть ) сделай рекомендации через теги как в
#  первом проекте в книги антонио миле python в примере
from lesson.models import Lesson


def index(request):
    """Тестовая функция"""
    all_lessons = Lesson.objects.annotate(words_count=Count('words'))  # Аннотация создаем "на лету" поле с количеством
    # слов
    return render(request, 'lesson/list.html', {'all_lessons': all_lessons})


def detail(request, id):
    lesson = Lesson.objects.get(id=id)

    return render(request, 'lesson/detail.html', {'lesson': lesson, })
