# Generated by Django 5.1 on 2025-01-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_category_course_delete_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.FileField(upload_to='category_icons/'),
        ),
    ]
