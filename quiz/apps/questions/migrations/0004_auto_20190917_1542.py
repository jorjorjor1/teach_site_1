# Generated by Django 2.2.1 on 2019-09-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_correct_var'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_var',
            field=models.CharField(max_length=200, verbose_name='Правильный вариант'),
        ),
    ]
