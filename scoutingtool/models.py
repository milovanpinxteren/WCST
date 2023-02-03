from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class PlayerPositions(models.Model):
    position = models.CharField(max_length=250)
    abbreviation = models.CharField(max_length=2)

    def __str__(self):
        return self.position


class GeneralPlayerInfo(models.Model):
    player_name = models.CharField(max_length=250)
    position = models.ForeignKey(PlayerPositions, on_delete=models.PROTECT, default='', blank=True)
    player_age = models.IntegerField(default=0, validators=[MaxValueValidator(50), MinValueValidator(15)])
    mins_played_per_game = models.FloatField(default=0, validators=[MaxValueValidator(150), MinValueValidator(0)])

    def __str__(self):
        return self.player_name


class Shooting(models.Model):
    player = models.ForeignKey(GeneralPlayerInfo, on_delete=models.CASCADE, default='', blank=True)
    goals_per_90_mins = models.FloatField(null=True, blank=True)
    shots_shots_per_90_mins = models.FloatField(null=True, blank=True)
