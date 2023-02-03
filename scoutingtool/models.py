from django.db import models


class PlayerPositions(models.Model):
    position = models.CharField(max_length=250)
    abbreviation = models.CharField(max_length=2)

    def __str__(self):
        return self.position

class GeneralPlayerInfo(models.Model):
    player_name = models.CharField(max_length=250)
    position = models.ForeignKey(PlayerPositions, on_delete=models.PROTECT, default='', blank=True)

    def __str__(self):
        return self.player_name


class Shooting(models.Model):
    player = models.ForeignKey(GeneralPlayerInfo, on_delete=models.CASCADE, default='', blank=True)
    goals = models.IntegerField(null=True, blank=True)
    shots = models.IntegerField(null=True, blank=True)