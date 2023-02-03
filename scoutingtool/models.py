from django.db import models


class PlayerData(models.Model):
    player_name = models.CharField(max_length=250)