# Generated by Django 5.0.2 on 2024-02-25 09:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_song_image_alter_song_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]