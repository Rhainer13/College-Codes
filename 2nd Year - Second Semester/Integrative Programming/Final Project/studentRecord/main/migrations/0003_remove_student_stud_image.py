# Generated by Django 5.0.6 on 2024-06-03 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_student_stud_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='stud_image',
        ),
    ]
