# Generated by Django 2.1 on 2018-10-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
