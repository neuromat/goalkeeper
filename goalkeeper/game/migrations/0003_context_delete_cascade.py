# Generated by Django 2.2 on 2019-06-03 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_code_and_name_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='context',
            name='goalkeeper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.GoalkeeperGame'),
        ),
        migrations.AlterField(
            model_name='probability',
            name='context',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Context'),
        ),
    ]
