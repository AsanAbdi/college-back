from django.db import models


class Email_sending(models.Model):
    receiver = models.EmailField(max_length=254, verbose_name='Получатель')

    # class Meta:
    #     verbose_name='Получатель вопросов'
    #     verbose_name_plural='Получатель вопросов'


class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')
    
    # class Meta:
    #     verbose_name='Вопрос/Ответ'
    #     verbose_name_plural='Вопросы/Ответы'


class Contact_information(models.Model):
    class TypeChoice(models.TextChoices):
        number = "number"
        email = "email"
        address = "address"
        extra_number = "extra number"
    title = models.CharField(max_length=255, verbose_name='Название')
    type = models.CharField(max_length=20, choices=TypeChoice.choices, verbose_name="Тип")
    text = models.TextField(verbose_name='Текст')


class Sertificate(models.Model):
    image = models.FileField(verbose_name='Картинка', upload_to='sertificates')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')


class Images_for_multimedia(models.Model):
    class TypeChoice(models.TextChoices):
        graduates = "graduates"
        video = "video"
        picture = "picture"
    image = models.FileField(verbose_name='Картинка', upload_to='images_for_multimedia')
    title = models.CharField(max_length=255, verbose_name='Название')
    link = models.URLField(max_length=500, verbose_name='Ссылка на видео')
    type = models.CharField(max_length=20, choices=TypeChoice.choices, verbose_name="Тип")


class Contact(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    role = models.CharField(max_length=100, verbose_name='Должность')
    email = models.EmailField(max_length=255, verbose_name='Почта')
    contact = models.CharField(max_length=255, verbose_name='Контакты')


class Block_of_contact(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    contact = models.CharField(max_length=255, verbose_name='Контакты')
    email = models.EmailField(max_length=255, verbose_name='Почта')


class Lecturer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    avatar = models.FileField(upload_to='avatars', verbose_name='Фотография')
    age = models.IntegerField(verbose_name='Возраст')
    bio = models.TextField(verbose_name="Информация")
    subject = models.CharField(max_length=255, verbose_name='Предмет')


class Sample(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    file = models.FileField(verbose_name='Файл', upload_to='samples')