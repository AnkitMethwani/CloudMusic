# Generated by Django 2.0.7 on 2018-07-28 23:06

import album.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0013_auto_20180729_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumcreate',
            name='album_logo',
            field=models.ImageField(default='img/portfolio/xyz.jpg', upload_to=album.models.upload_image_path),
        ),
    ]