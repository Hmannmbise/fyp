# Generated by Django 3.0 on 2022-04-27 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_backend', '0003_auto_20220427_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_email',
        ),
    ]