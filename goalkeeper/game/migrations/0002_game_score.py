# Generated by Django 2.2 on 2019-07-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]