# Generated by Django 4.1.7 on 2023-07-03 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_remove_course_lesson'),
        ('lesson', '0005_remove_lesson_lesson_lesson_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Курсы'),
        ),
    ]
