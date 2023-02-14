from django.contrib import admin

from scoutingtool.models import GeneralPlayerInfo, PlayerPositions, Shooting, Passing, Defense, Possession, \
    DuelsandOffside


@admin.register(PlayerPositions)
class PlayerPositionsAdmin(admin.ModelAdmin):
    list_display = ['position', 'abbreviation']


@admin.register(GeneralPlayerInfo)
class GeneralPlayerInfoAdmin(admin.ModelAdmin):
    list_display = ['player_name']

@admin.register(Shooting)
class ShootingAdmin(admin.ModelAdmin):
    list_display = ['player', 'goals_per_90_mins', 'shots_per_90_mins']

@admin.register(Passing)
class PassingAdmin(admin.ModelAdmin):
    list_display = ['player', 'passes_per_90_mins', 'passes_completed_percentage']

@admin.register(Defense)
class DefenseAdmin(admin.ModelAdmin):
    list_display = ['player', 'tackles_per_90_mins', 'tackles_won_per_90_mins']

@admin.register(Possession)
class PossessionAdmin(admin.ModelAdmin):
    list_display = ['player', 'touches_per_90_mins', 'dribbles_per_90_mins']

@admin.register(DuelsandOffside)
class DuelsandOffsideAdmin(admin.ModelAdmin):
    list_display = ['player', 'yellow_cards_per_90_mins', 'fouls_per_90_mins']