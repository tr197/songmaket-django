# Generated by Django 5.0.2 on 2024-02-26 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0004_song_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='views',
            new_name='view_count',
        ),
    ]
