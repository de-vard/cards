from django import forms
from django.forms import ModelForm
from .models import WrongCards


class WrongCardsForm(ModelForm):
    class Meta:
        model = WrongCards
        fields = ('mistake_in', 'error_text',)
        # fields = '__all__'
