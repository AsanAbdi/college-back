from django.db import models
from django.utils.timezone import now


class Admission_date(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    event_date = models.DateTimeField(verbose_name='Дата', default=now)
    description = models.TextField(verbose_name='Текст')


class Specialtie(models.Model):
    class TypeChoice(models.TextChoices):
        distance = "distance"
        full_time = "full_time"
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Текст')
    study_time = models.FileField(verbose_name="Расписание", upload_to='Specialties')
    type = models.CharField(verbose_name='Тип образования', max_length=255, choices=TypeChoice.choices)
    budget = models.CharField(max_length=255, verbose_name='Бюджет/контрак/другое')
    mini_description = models.TextField(verbose_name='Краткое описание')


class Scholorship_grant(models.Model):
    class TypeChoice(models.TextChoices):
        scholorship = "scholorship"
        grant = "grant"
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Текст')
    type = models.CharField(verbose_name='Стипендия/грант', max_length=255, choices=TypeChoice.choices)


class Courses_programms(models.Model):
    class TypeChoice(models.TextChoices):
        student = "student"
        lecturer = "lecturer"
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Текст')
    duration = models.CharField(max_length=255, verbose_name='Длительность')
    mini_description = models.TextField(verbose_name='Краткое описание')
    price = models.IntegerField(verbose_name='Цена')
    type = models.CharField(max_length=25, verbose_name='Для кого', choices=TypeChoice.choices)


class Schedule(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    file = models.FileField(verbose_name='Файл', upload_to='schedule')
    