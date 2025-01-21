# Generated by Django 5.1 on 2025-01-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_course_author_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='languages',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('es', 'Spanish'), ('it', 'Italian'), ('de', 'German')], default='en', max_length=5, null=True),
        ),
    ]
