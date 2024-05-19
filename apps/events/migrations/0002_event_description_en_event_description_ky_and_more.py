# Generated by Django 5.0.4 on 2024-05-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='description_ky',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='duration_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Длительность'),
        ),
        migrations.AddField(
            model_name='event',
            name='duration_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Длительность'),
        ),
        migrations.AddField(
            model_name='event',
            name='duration_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Длительность'),
        ),
        migrations.AddField(
            model_name='event',
            name='location_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Локация'),
        ),
        migrations.AddField(
            model_name='event',
            name='location_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Локация'),
        ),
        migrations.AddField(
            model_name='event',
            name='location_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Локация'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
    ]