# Generated by Django 5.1 on 2025-01-21 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_course_languages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='languages',
        ),
    ]
