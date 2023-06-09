# Generated by Django 4.1.7 on 2023-05-16 12:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=100, verbose_name='Термин')),
                ('transcription', models.CharField(max_length=100, verbose_name='Транскрипция')),
                ('definition', models.CharField(max_length=100, verbose_name='Определение')),
                ('slug', models.SlugField(max_length=250, verbose_name='Слаг')),
                ('audi', models.FileField(upload_to='audi/%Y/%m/%d', validators=[django.core.validators.RegexValidator(regex='.mp3')], verbose_name='Произношение')),
                ('audio_rus', models.FileField(blank=True, upload_to='audi/%Y/%m/%d', validators=[django.core.validators.RegexValidator(regex='.mp3')], verbose_name='Произношение по русски')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата последнего редактирования')),
            ],
            options={
                'verbose_name': 'Карточку',
                'verbose_name_plural': 'Карточки',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='WrongCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mistake_in', models.CharField(choices=[(None, 'Выберите в чем ошибка'), ('a', 'терминe'), ('b', 'определение'), ('c', 'произношение')], max_length=3, verbose_name='Ошибка в')),
                ('error_text', models.TextField(verbose_name='Подробнее об ошибки')),
            ],
        ),
    ]
