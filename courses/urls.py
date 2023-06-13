from django.urls import path
from courses import views

app_name = 'course'

urlpatterns = [
    path('', views.list_courses, name='list'),
    path('<int:id>/', views.detail_course, name='detail'),
    path('new/', views.CourseCreateView.as_view(), name='create')
]
