# Generated by Django 4.1.7 on 2023-05-04 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_alter_card_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='slug',
            field=models.SlugField(max_length=250, verbose_name='Слаг'),
        ),
    ]