# Generated by Django 5.1 on 2025-01-18 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_course_rename_categories_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='instructors/images/')),
                ('name', models.CharField(max_length=128)),
                ('role', models.CharField(max_length=128)),
                ('single_star', models.FileField(upload_to='instructor/icons/')),
                ('rating', models.FloatField(default=0.0, help_text='Instructor rating out of 5.0')),
                ('total_students', models.PositiveIntegerField(help_text='Total number of students taught')),
            ],
            options={
                'verbose_name': 'Instructor',
                'verbose_name_plural': 'Instructors',
                'db_table': 'instructors',
                'ordering': ['id'],
            },
        ),
    ]
