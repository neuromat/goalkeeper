from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

FINAL_SCORE = (
    ('long', _('Long')),
    ('short', _('Short')),
    ('none', _('None')),
)

NO = 'no'
YES = 'yes'
YES_NO_ANSWER = (
    (NO, _('No')),
    (YES, _('Yes')),
)

TWO = 2
THREE = 3
DIRECTIONS_CHOICES = (
    (TWO, _('2 - left and right')),
    (THREE, _('3 - left, center and right')),
)


class Level(models.Model):
    """ An instance of this class is used to identify the level of a participant and also the level of the opponent. """
    name = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.name)


class GameConfig(models.Model):
    """ An instance of this class is an opponent. """
    level = models.ForeignKey(Level, verbose_name=_('Level'), on_delete=models.PROTECT)
    code = models.CharField(_('Code'), max_length=50, unique=True)
    name = models.CharField(_('Name'), max_length=100, unique=True)
    is_public = models.CharField(_('Is it public?'), max_length=3, choices=YES_NO_ANSWER, default=NO)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Configuration')
        verbose_name_plural = _('Configurations')
        ordering = ('name',)


class Game(models.Model):
    config = models.ForeignKey(GameConfig, on_delete=models.PROTECT)
    phase = models.IntegerField()
    number_of_directions = models.IntegerField(choices=DIRECTIONS_CHOICES, default=THREE)
    number_of_plays = models.PositiveIntegerField()
    min_hits = models.PositiveIntegerField(blank=True, null=True)
    min_hits_in_seq = models.PositiveIntegerField(blank=True, null=True)
    sequence = models.CharField(max_length=255, blank=True)
    read_seq = models.BooleanField()
    plays_to_relax = models.PositiveIntegerField(default=0)
    play_pause = models.BooleanField()
    play_pause_key = models.CharField(max_length=10, blank=True)
    player_time = models.FloatField(default=1.0)
    celebration_time = models.FloatField(default=1.0)
    score_board = models.BooleanField()
    final_score_board = models.CharField(max_length=5, choices=FINAL_SCORE, default='short')
    game_type = models.CharField(max_length=2)
    left_key = models.CharField(max_length=20, blank=True)
    center_key = models.CharField(max_length=20, blank=True)
    right_key = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.config.name + ' - ' + self.game_type


class WarmUp(Game):
    """ An instance of this class is a Warm Up game. """

    def __str__(self):
        return self.config.name + ' - ' + str(self.sequence)

    # Sets the type of the game.
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.game_type = 'AQ'
        super(WarmUp, self).save(*args, **kwargs)


class GoalkeeperGame(Game):
    """ An instance of this class is a Goalkeeper game. """
    depth = models.IntegerField(blank=True, null=True)
    seq_step_det_or_prob = models.CharField(max_length=255, blank=True)
    create_seq_manually = models.CharField(max_length=3, choices=YES_NO_ANSWER, default=NO)
    show_history = models.BooleanField()
    send_markers_eeg = models.CharField(max_length=30, blank=True)
    port_eeg_serial = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.config.name + ' - ' + str(self.phase)

    # Sets the type of the game.
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.game_type = 'JG'
        super(GoalkeeperGame, self).save(*args, **kwargs)


class Context(models.Model):
    """ An instance of this class is a context of a context tree. """
    goalkeeper = models.ForeignKey(GoalkeeperGame, on_delete=models.CASCADE)
    path = models.CharField(max_length=5)
    is_context = models.CharField(max_length=5)
    analyzed = models.BooleanField(default=False)


class Probability(models.Model):
    """ An instance of this class is the probability of a given direction in a given context.  """
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    direction = models.IntegerField()
    value = models.FloatField()
