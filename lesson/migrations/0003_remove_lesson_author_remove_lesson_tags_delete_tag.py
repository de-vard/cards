# Generated by Django 4.1.7 on 2023-06-09 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_lesson_author_alter_lesson_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='author',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]