from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from cards.forms import WrongCardsForm
from cards.models import Card


class CardDetailView(FormMixin, DetailView):
    model = Card
    template_name = 'cards/detail.html'
    success_message = 'Ваше сообщение об ошибке получено. Мы обязательно займемся этим.'
    form_class = WrongCardsForm

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(CardDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return super(CardDetailView, self).form_valid(form)

    def form_valid(self, form):
        form = form.save(commit=False)
        form.author = self.request.user
        form.card = self.get_object()
        form.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)  # Выводим сообщение
        return super(CardDetailView, self).form_valid(form)


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
