from django.urls import path
from cards import views

urlpatterns = [
    path('', views.CardsListView.as_view(), name='index'),
    path('<int:id>/', views.detail_card, name='detail'),
    path('mistake/<int:id>/', views.mistake_card, name='mistake'),

]
