# Generated by Django 2.2 on 2019-06-28 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=5)),
                ('is_context', models.CharField(max_length=5)),
                ('analyzed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.IntegerField()),
                ('number_of_directions', models.IntegerField(choices=[(2, '2 - left and right'),
                                                                      (3, '3 - left, center and right')], default=3)),
                ('number_of_plays', models.PositiveIntegerField()),
                ('min_hits', models.PositiveIntegerField(blank=True, null=True)),
                ('min_hits_in_seq', models.PositiveIntegerField(blank=True, null=True)),
                ('sequence', models.CharField(blank=True, max_length=255)),
                ('read_seq', models.BooleanField()),
                ('plays_to_relax', models.PositiveIntegerField(default=0)),
                ('play_pause', models.BooleanField()),
                ('play_pause_key', models.CharField(blank=True, max_length=10)),
                ('player_time', models.FloatField(default=1.0)),
                ('celebration_time', models.FloatField(default=1.0)),
                ('score_board', models.BooleanField()),
                ('final_score_board', models.CharField(choices=[('long', 'Long'), ('short', 'Short'), ('none', 'None')],
                                                       default='short', max_length=5)),
                ('game_type', models.CharField(max_length=2)),
                ('left_key', models.CharField(blank=True, max_length=20)),
                ('center_key', models.CharField(blank=True, max_length=20)),
                ('right_key', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoalkeeperGame',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                  parent_link=True, primary_key=True, serialize=False, to='game.Game')),
                ('depth', models.IntegerField(blank=True, null=True)),
                ('seq_step_det_or_prob', models.CharField(blank=True, max_length=255)),
                ('create_seq_manually', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no',
                                                         max_length=3)),
                ('show_history', models.BooleanField()),
                ('send_markers_eeg', models.CharField(blank=True, max_length=30)),
                ('port_eeg_serial', models.CharField(blank=True, max_length=30)),
            ],
            bases=('game.game',),
        ),
        migrations.CreateModel(
            name='WarmUp',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                  parent_link=True, primary_key=True, serialize=False, to='game.Game')),
            ],
            bases=('game.game',),
        ),
        migrations.CreateModel(
            name='Probability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.IntegerField()),
                ('value', models.FloatField()),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Context')),
            ],
        ),
        migrations.CreateModel(
            name='GameConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Code')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('is_public', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=3,
                                               verbose_name='Is it public?')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                 to=settings.AUTH_USER_MODEL)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.Level',
                                            verbose_name='Level')),
            ],
            options={
                'verbose_name': 'Configuration',
                'verbose_name_plural': 'Configurations',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='game',
            name='config',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.GameConfig'),
        ),
        migrations.AddField(
            model_name='context',
            name='goalkeeper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.GoalkeeperGame'),
        ),
    ]
