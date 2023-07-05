from django import forms
from lesson import models


class LessonCreationForm(forms.ModelForm):
    """Форма создания урока"""

    class Meta:
        model = models.Lesson
        fields = ['title', 'word_eng', 'word_rus', 'image', ]
