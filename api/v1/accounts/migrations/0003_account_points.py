# Generated by Django 3.1.4 on 2020-12-26 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201220_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
