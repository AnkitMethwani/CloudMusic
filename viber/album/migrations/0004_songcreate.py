# Generated by Django 2.0.7 on 2018-07-26 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_albumcreate_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongCreate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=250)),
                ('is_favorite', models.BooleanField(default=False)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.AlbumCreate')),
            ],
        ),
    ]
