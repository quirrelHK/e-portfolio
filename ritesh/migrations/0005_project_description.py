# Generated by Django 5.0.6 on 2024-05-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ritesh', '0004_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='Description'),
            preserve_default=False,
        ),
    ]