# Generated by Django 3.2 on 2024-02-17 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0010_alter_customuser_bio'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='customuser',
            name='unique_user',
        ),
    ]
