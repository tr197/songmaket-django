# Generated by Django 5.0.2 on 2024-02-26 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0003_song_created_at_song_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='views',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
