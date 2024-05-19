# Generated by Django 5.0.4 on 2024-05-19 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abouts', '0002_alter_email_sending_options_alter_faq_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block_of_contact',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='block_of_contact',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='block_of_contact',
            name='title_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='block_of_contact',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='role_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='role_ky',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='role_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='contact_information',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='contact_information',
            name='text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='contact_information',
            name='text_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='contact_information',
            name='text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='contact_information',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='contact_information',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='contact_information',
            name='title_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='contact_information',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(blank=True, null=True, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_en',
            field=models.TextField(blank=True, null=True, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='images_for_multimedia',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='images_for_multimedia',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='images_for_multimedia',
            name='title_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='images_for_multimedia',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='bio_en',
            field=models.TextField(blank=True, null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='bio_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='bio_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='name_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='name_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='name_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='subject_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='subject_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='subject_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='description_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='title_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='sertificate',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='sertificate',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='sertificate',
            name='description_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='sertificate',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='sertificate',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='sertificate',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='sertificate',
            name='title_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='sertificate',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
    ]