from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.db.models import Count
from django.views.generic import CreateView

from courses.models import Course


def list_courses(request):
    """Тестовая функция"""
    all_courses = Course.objects.annotate(lesson_count=Count('lesson'))  # Аннотация создаем "на лету" поле с
    # количеством уроков
    return render(request, 'courses/list.html', {'all_courses': all_courses})


def detail_course(request, id):
    """Тестовая функция"""
    course = Course.objects.get(id=id)
    return render(request, 'courses/detail.html', {'course': course})


class CourseCreateView(LoginRequiredMixin, CreateView):
    """ Класс для создания курса """
    model = Course
    fields = ['level', 'title']  # атрибут, последовательность имен полей модели, которые должны присутствовать в форме
    template_name = 'courses/create.html'
    login_url = 'account_login'  # перенаправляет если пользователь не авторизирован

    def form_valid(self, form):
        """ Метод автоматически устанавливает автора """
        form.instance.author = self.request.user
        return super().form_valid(form)
