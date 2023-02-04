from django import forms

from scoutingtool.choices import *
from scoutingtool.models import PlayerPositions


class CritereaSelectorForm(forms.Form):
    #################################################General Info#####################################################
    player_position = forms.ModelChoiceField(queryset=PlayerPositions.objects.all().order_by('id'), empty_label="Select Position")
    player_age_min = forms.IntegerField(required=False)
    player_age_min_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    player_age_max = forms.IntegerField(required=False)
    player_age_max_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    #################################################Goals and Shooting#####################################################
    goals = forms.ChoiceField(required=False, choices=GOALS_CHOICES)
    goals_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    shots = forms.ChoiceField(required=False, choices=SHOTS_CHOICES)
    shots_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    shots_on_target = forms.ChoiceField(required=False, choices=SHOTS_ON_TARGET_CHOICES)
    shots_on_target_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    goals_per_shot = forms.ChoiceField(required=False, choices=GOALS_PER_SHOT_CHOICES)
    goals_per_shot_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    penalty_killer = forms.ChoiceField(required=False, choices=PENALTY_KILLER_CHOICES)
    penalty_killer_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    #################################################Passing#####################################################
