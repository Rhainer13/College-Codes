# Generated by Django 5.0.6 on 2024-06-03 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]