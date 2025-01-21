# Generated by Django 5.1 on 2025-01-21 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_course_languages'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification', models.TextField()),
                ('syllabus', models.TextField()),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='web.course')),
            ],
        ),
    ]
