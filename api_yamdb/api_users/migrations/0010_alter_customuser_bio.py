# Generated by Django 3.2 on 2024-02-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0009_remove_customuser_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
    ]