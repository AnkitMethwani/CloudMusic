# Generated by Django 2.0.7 on 2018-07-26 16:51

import album.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_albumcreate_album_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumcreate',
            name='album_logo',
            field=models.FileField(blank=True, null=True, upload_to=album.models.upload_image_path),
        ),
    ]
