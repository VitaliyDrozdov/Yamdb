# Generated by Django 3.2 on 2024-02-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]