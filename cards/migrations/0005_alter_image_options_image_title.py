# Generated by Django 4.1.7 on 2023-07-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_rename_photo_card_image_image_related_words'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default=1, max_length=50, verbose_name='Название'),
            preserve_default=False,
        ),
    ]
