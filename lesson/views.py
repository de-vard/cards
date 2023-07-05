from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse

# TODO:Всуну пока сюда так как не знаю куда всунуть ) сделай рекомендации через теги как в
#  первом проекте в книги антонио миле python в примере
from django.views.generic import CreateView

from courses.models import Course
from lesson.forms import LessonCreationForm
from lesson.models import Lesson


def index(request):
    """Тестовая функция"""
    all_lessons = Lesson.objects.annotate(words_count=Count('word_eng'))  # Аннотация создаем "на лету" поле с
    # количеством слов
    return render(request, 'lesson/list.html', {'all_lessons': all_lessons})


def detail(request, id):
    lesson = Lesson.objects.get(id=id)
    return render(request, 'lesson/detail.html', {'lesson': lesson, })


class LessonCreateView(CreateView):
    """Создание уроков"""
    form_class = LessonCreationForm  # ссылка на класс формы, связанной с моделью
    template_name = 'lesson/create.html'

    def form_valid(self, form):  # Выполняются действия перед сохранением данных
        """Подставляю значение курса автоматически """
        form.instance.course = Course.objects.get(pk=self.kwargs['pk'])  # instance - использовать для указания
        # объекта, который должен быть обновлен/изменен
        return super().form_valid(form)

    def get_success_url(self):
        """Перенаправляю после сохранения """
        return reverse('course:detail', args=[self.object.course.id])  # self.object является экземпляром созданного
        # объекта, который был сохранен в базе данных после успешной валидации формы. Мы создали объект и можем через
        # него получить значение id
