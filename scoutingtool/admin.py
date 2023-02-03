from django.contrib import admin

from scoutingtool.models import PlayerData


@admin.register(PlayerData)
class PlayerDataAdmin(admin.ModelAdmin):
    list_display = ['player_name']

