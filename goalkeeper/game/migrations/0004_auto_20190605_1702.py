# Generated by Django 2.2 on 2019-06-05 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20190605_1659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gameconfig',
            options={'ordering': ('name',), 'verbose_name': 'Configuration', 'verbose_name_plural': 'Configurations'},
        ),
    ]
