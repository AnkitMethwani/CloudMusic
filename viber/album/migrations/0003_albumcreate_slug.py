# Generated by Django 2.0.7 on 2018-07-25 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20180725_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumcreate',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
