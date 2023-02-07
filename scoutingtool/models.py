from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class PlayerPositions(models.Model):
    position = models.CharField(max_length=250)
    abbreviation = models.CharField(max_length=2)

    def __str__(self):
        return self.position


class GeneralPlayerInfo(models.Model):
    player_name = models.CharField(max_length=250)
    position = models.ForeignKey(PlayerPositions, on_delete=models.PROTECT, default=1)
    player_age = models.IntegerField(default=0, validators=[MaxValueValidator(50), MinValueValidator(0)])
    mins_played_per_game = models.FloatField(default=0, validators=[MaxValueValidator(150), MinValueValidator(0)])

    def __str__(self):
        return self.player_name


class Shooting(models.Model):
    player = models.ForeignKey(GeneralPlayerInfo, on_delete=models.CASCADE, default='', blank=True)
    goals_per_90_mins = models.FloatField(null=True, blank=True)
    shots_per_90_mins = models.FloatField(null=True, blank=True)
    shots_on_target_per_90_mins = models.FloatField(null=True, blank=True)
    goals_per_shot = models.FloatField(null=True, blank=True)
    penalty_success_rate = models.FloatField(null=True, blank=True) #only if more than >3 penalties taken

class Passing(models.Model):
    player = models.ForeignKey(GeneralPlayerInfo, on_delete=models.CASCADE, default='', blank=True)
    passes_per_90_mins = models.FloatField(null=True, blank=True)
    passes_completed_percentage = models.FloatField(null=True, blank=True)
    passes_short_percentage = models.FloatField(null=True, blank=True)
    passes_medium_percentage = models.FloatField(null=True, blank=True)
    passes_long_percentage = models.FloatField(null=True, blank=True)
    assists_per_90_mins = models.FloatField(null=True, blank=True)
    assisted_shots_per_90_mins = models.FloatField(null=True, blank=True)
    crosses_per_90_mins = models.FloatField(null=True, blank=True)

class Defense(models.Model):
    player = models.ForeignKey(GeneralPlayerInfo, on_delete=models.CASCADE, default='', blank=True)
    tackles_per_90_mins = models.FloatField(null=True, blank=True)
    tackles_won_per_90_mins = models.FloatField(null=True, blank=True)
    blocks_per_90_mins = models.FloatField(null=True, blank=True)
    interceptions_per_90_mins = models.FloatField(null=True, blank=True)
    clearences_per_90_mins = models.FloatField(null=True, blank=True)
    errors_per_90_mins = models.FloatField(null=True, blank=True)


class Possession(models.Model):
    player = models.ForeignKey(GeneralPlayerInfo, on_delete=models.CASCADE, default='', blank=True)
    shot_creating_actions_per_90_mins = models.FloatField(null=True, blank=True)
    goal_creating_actions_per_90_mins = models.FloatField(null=True, blank=True)
    touches_per_90_mins = models.FloatField(null=True, blank=True)
    dribbles_per_90_mins = models.FloatField(null=True, blank=True)
    completed_dribbles_percentage = models.FloatField(null=True, blank=True)
    miscontrols_per_90_mins = models.FloatField(null=True, blank=True)
    dispossessed_per_90_mins = models.FloatField(null=True, blank=True)

class DuelsandOffside(models.Model):
    player = models.ForeignKey(GeneralPlayerInfo, on_delete=models.CASCADE, default='', blank=True)
    yellow_cards_per_90_mins = models.FloatField(null=True, blank=True)
    red_cards_per_90_mins = models.FloatField(null=True, blank=True)
    fouls_per_90_mins = models.FloatField(null=True, blank=True)
    fouled_per_90_mins = models.FloatField(null=True, blank=True)
    offsides_per_90_mins = models.FloatField(null=True, blank=True)
    aerials_per_90_mins = models.FloatField(null=True, blank=True)
    aerials_won_percentage = models.FloatField(null=True, blank=True)