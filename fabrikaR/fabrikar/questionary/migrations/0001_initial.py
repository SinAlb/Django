# Generated by Django 3.2.5 on 2021-07-16 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название опроса')),
                ('start_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата старта')),
                ('end_date', models.DateTimeField(verbose_name='Дата окончания')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
                'ordering': ['-start_at'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Текст вопроса')),
                ('question_type', models.CharField(max_length=250, verbose_name='Тип ответов')),
                ('questionary_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='questionary.questionary', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Текст ответа')),
                ('question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='questionary.question', verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]