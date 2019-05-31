# Generated by Django 2.2 on 2019-05-31 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameconfig',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='gameconfig',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='gameconfig',
            unique_together=set(),
        ),
    ]