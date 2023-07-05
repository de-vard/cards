# Generated by Django 4.1.7 on 2023-07-05 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_alter_image_options_image_title'),
        ('lesson', '0007_rename_words_lesson_redy_words_lesson_word_eng_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cards.image', verbose_name='Фото'),
        ),
    ]
