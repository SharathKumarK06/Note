# Generated by Django 5.1 on 2025-04-09 10:58

import django.utils.timezone
import noteapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='categories',
            field=models.ManyToManyField(default=noteapp.models.Category.get_default_pk, related_name='notes', to='noteapp.category'),
        ),
    ]
