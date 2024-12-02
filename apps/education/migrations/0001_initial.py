# Generated by Django 5.0.4 on 2024-12-02 17:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission_date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('event_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_en', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Courses_programms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_en', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
                ('duration', models.CharField(blank=True, max_length=255, null=True, verbose_name='Длительность')),
                ('duration_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Длительность')),
                ('duration_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Длительность')),
                ('duration_ky', models.CharField(blank=True, max_length=255, null=True, verbose_name='Длительность')),
                ('mini_description', models.TextField(verbose_name='Краткое описание')),
                ('mini_description_ru', models.TextField(null=True, verbose_name='Краткое описание')),
                ('mini_description_en', models.TextField(null=True, verbose_name='Краткое описание')),
                ('mini_description_ky', models.TextField(null=True, verbose_name='Краткое описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('type', models.CharField(choices=[('student', 'Student'), ('lecturer', 'Lecturer')], max_length=25, verbose_name='Для кого')),
                ('image', models.FileField(upload_to='coursesProgramms', verbose_name='Файл')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('file', models.FileField(upload_to='schedule', verbose_name='Файл')),
            ],
        ),
        migrations.CreateModel(
            name='Scholorship_grant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_en', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
                ('type', models.CharField(choices=[('scholorship', 'Scholorship'), ('grant', 'Grant')], max_length=255, verbose_name='Стипендия/грант')),
            ],
        ),
        migrations.CreateModel(
            name='Specialtie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_en', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
                ('study_time', models.FileField(upload_to='Specialties', verbose_name='Расписание')),
                ('type', models.CharField(choices=[('distance', 'Distance'), ('full_time', 'Full Time')], max_length=255, verbose_name='Тип образования')),
                ('budget', models.CharField(max_length=255, verbose_name='Бюджет/контрак/другое')),
            ],
        ),
    ]
