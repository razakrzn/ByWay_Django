# Generated by Django 5.1.2 on 2024-10-19 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_alter_instructors_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['id']},
        ),
    ]
