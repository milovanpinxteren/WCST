from django.contrib import admin

from scoutingtool.models import GeneralPlayerInfo, PlayerPositions, Shooting


@admin.register(PlayerPositions)
class PlayerPositionsAdmin(admin.ModelAdmin):
    list_display = ['position', 'abbreviation']

@admin.register(GeneralPlayerInfo)
class GeneralPlayerInfoAdmin(admin.ModelAdmin):
    list_display = ['player_name']

@admin.register(Shooting)
class ShootingAdmin(admin.ModelAdmin):
    list_display = ['player', 'goals']