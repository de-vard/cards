from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('<int:pk>/', views.UserDetailView.as_view(), name='detail'),
]
