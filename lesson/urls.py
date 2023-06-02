from django.urls import path
from lesson import views

app_name = 'lesson'

urlpatterns = [
    path('', views.index, name='list'),
    path('<int:id>/', views.detail, name='detail')

]
