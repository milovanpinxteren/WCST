from django import forms

from scoutingtool.choices import *
from scoutingtool.models import PlayerPositions


class CritereaSelectorForm(forms.Form):
    #################################################General Info#####################################################
    player_position = forms.ModelChoiceField(queryset=PlayerPositions.objects.all().order_by('id'), empty_label="Select Position")
    player_age_min = forms.IntegerField(initial=0)
    # player_age_min_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    player_age_max = forms.IntegerField(initial=50)
    # player_age_max_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    #################################################Goals and Shooting#####################################################
    goals_per_90_mins = forms.ChoiceField(required=False, choices=GOALS_CHOICES)
    goals_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    shots_per_90_mins = forms.ChoiceField(required=False, choices=SHOTS_CHOICES)
    shots_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    shots_on_target_per_90_mins = forms.ChoiceField(required=False, choices=SHOTS_ON_TARGET_CHOICES)
    shots_on_target_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    goals_per_shot = forms.ChoiceField(required=False, choices=GOALS_PER_SHOT_CHOICES)
    goals_per_shot_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    penalty_success_rate = forms.ChoiceField(required=False, choices=PENALTY_KILLER_CHOICES)
    penalty_success_rate_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    #####################################################Passing#######################################################
    passes_per_90_mins = forms.ChoiceField(required=False, choices=PASSES_PER_90_MINS_CHOICES)
    passes_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    passes_completed_percentage = forms.ChoiceField(required=False, choices=PASSES_COMPLETED_CHOICES)
    passes_completed_percentage_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    passes_short_percentage = forms.ChoiceField(required=False, choices=PASSES_SHORT_CHOICES)
    passes_short_percentage_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    passes_medium_percentage = forms.ChoiceField(required=False, choices=PASSES_MEDIUM_CHOICES)
    passes_medium_percentage_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    passes_long_percentage = forms.ChoiceField(required=False, choices=PASSES_LONG_CHOICES)
    passes_long_percentage_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    assists_per_90_mins = forms.ChoiceField(required=False, choices=ASSISTS_PER_90_MINS_CHOICES)
    assists_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    assisted_shots_per_90_mins = forms.ChoiceField(required=False, choices=ASSISTED_SHOTS_PER_90_MINS_CHOICES)
    assisted_shots_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    crosses_per_90_mins = forms.ChoiceField(required=False, choices=CROSSES_PER_90_MINS_CHOICES)
    crosses_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)