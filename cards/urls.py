from django.urls import path
from cards import views

app_name = 'card'

urlpatterns = [
    path('', views.CardsListView.as_view(), name='index'),
    path('<int:pk>/', views.CardDetailView.as_view(), name='detail'),

]
