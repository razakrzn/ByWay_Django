# Generated by Django 5.1.2 on 2024-10-15 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_category_instructor_language_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='name',
            new_name='languages',
        ),
    ]
