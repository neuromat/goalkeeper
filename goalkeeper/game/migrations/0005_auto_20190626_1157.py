# Generated by Django 2.2 on 2019-06-26 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20190626_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='min_plays',
            new_name='min_hits',
        ),
    ]
