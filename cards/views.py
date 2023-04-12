from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from cards.forms import WrongCardsForm
from cards.models import Card, WrongCards
from django.contrib import messages


def detail_card(request, id):
    """Просмотр отдельной карточки"""
    card = get_object_or_404(Card, id=id)
    form = WrongCardsForm()
    return render(request, 'cards/detail.html', {'card': card, 'form': form, })


def mistake_card(request, id):
    """Помечаем что каточка с ошибкой"""

    card = get_object_or_404(Card, id=id)
    wrong = WrongCards()
    if 'text' in request.POST:
        text_mistake = f" Имя: {request.user}\n Email: {request.user.email}\nОШИБКА ЗАКЛЮЧЕНА В ТОМ: {request.POST.get('text')}"
        wrong.card = card
        wrong.error_text = text_mistake
        wrong.save()
        messages.add_message(
            request, messages.SUCCESS,
            'Ваше сообщение об ошибке получено, мы займемся им в ближащее время и тобой. Я найду тебя мышь'
        )
    return redirect('detail', id=id)


class CardsListView(ListView):
    model = Card
    context_object_name = 'all_cards'
    template_name = 'cards/index.html'

    def get_queryset(self):
        """Переопределили queryset для поиска и сортировки"""
        query = self.request.GET.get('search')
        ordering = self.request.GET.get('sorted')
        ordering = ordering if ordering else '-created'  # по умолчанию сортирует по дате создания
        # Todo: Выведи логику в отдельный файл
        if query:
            object_list = self.model.objects.filter(
                Q(term__icontains=query) | Q(definition__icontains=query)
            ).order_by(ordering)
        else:
            object_list = self.model.objects.all().order_by(ordering)
        return object_list
