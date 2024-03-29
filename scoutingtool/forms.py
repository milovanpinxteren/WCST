from django import forms

from scoutingtool.choices import *
from scoutingtool.models import PlayerPositions


class CritereaSelectorForm(forms.Form):
    #################################################General Info#######################################################
    player_position = forms.ModelChoiceField(queryset=PlayerPositions.objects.all().order_by('id'), empty_label="Select Position")
    player_age_min = forms.IntegerField(initial=0)
    player_age_max = forms.IntegerField(initial=50)
    #################################################Goals and Shooting#################################################
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
    #####################################################Passing########################################################
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
    #####################################################Defense########################################################
    tackles_per_90_mins = forms.ChoiceField(required=False, choices=TACKLES_PER_90_MINS_CHOICES)
    tackles_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    tackles_won_per_90_mins = forms.ChoiceField(required=False, choices=TACKLES_WON_PER_90_MINS_CHOICES)
    tackles_won_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    blocks_per_90_mins = forms.ChoiceField(required=False, choices=BLOCKS_PER_90_MINS_CHOICES)
    blocks_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    interceptions_per_90_mins = forms.ChoiceField(required=False, choices=INTERCEPTIONS_PER_90_MINS_CHOICES)
    interceptions_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    clearences_per_90_mins = forms.ChoiceField(required=False, choices=CLEARENCES_PER_90_MINS_CHOICES)
    clearences_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    errors_per_90_mins = forms.ChoiceField(required=False, choices=ERRORS_PER_90_MINS_CHOICES)
    errors_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
#####################################################Possesion##########################################################
    shot_creating_actions_per_90_mins = forms.ChoiceField(required=False, choices=SHOT_CREATING_ACTIONS_PER_90_MINS_CHOICES)
    shot_creating_actions_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    goal_creating_actions_per_90_mins = forms.ChoiceField(required=False, choices=GOAL_CREATING_ACTIONS_PER_90_MINS_CHOICES)
    goal_creating_actions_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    touches_per_90_mins = forms.ChoiceField(required=False, choices=TOUCHES_PER_90_MINS_CHOICES)
    touches_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    dribbles_per_90_mins = forms.ChoiceField(required=False, choices=DRIBBLES_PER_90_MINS_CHOICES)
    dribbles_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    completed_dribbles_percentage = forms.ChoiceField(required=False, choices=COMPLETED_DRIBBLES_PER_90_MINS_CHOICES)
    completed_dribbles_percentage_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    miscontrols_per_90_mins = forms.ChoiceField(required=False, choices=MISCONTROLS_PER_90_MINS_CHOICES)
    miscontrols_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    dispossessed_per_90_mins = forms.ChoiceField(required=False, choices=DISPOSSESSED_PER_90_MINS_CHOICES)
    dispossessed_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
#####################################################DuelsandOffside####################################################
    yellow_cards_per_90_mins = forms.ChoiceField(required=False, choices=YELLOW_CARDS_PER_90_MINS_CHOICES)
    yellow_cards_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    red_cards_per_90_mins = forms.ChoiceField(required=False, choices=RED_CARDS_PER_90_MINS_CHOICES)
    red_cards_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    fouls_per_90_mins = forms.ChoiceField(required=False, choices=FOULS_PER_90_MINS_CHOICES)
    fouls_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    fouled_per_90_mins = forms.ChoiceField(required=False, choices=FOULED_PER_90_MINS_CHOICES)
    fouled_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    offsides_per_90_mins = forms.ChoiceField(required=False, choices=OFFSIDES_PER_90_MINS_CHOICES)
    offsides_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    aerials_per_90_mins = forms.ChoiceField(required=False, choices=AERIALS_PER_90_MINS_CHOICES)
    aerials_per_90_mins_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
    aerials_won_percentage = forms.ChoiceField(required=False, choices=AERIALS_WON_PER_90_MINS_CHOICES)
    aerials_won_percentage_importance = forms.ChoiceField(required=False, choices=IMPORTANCE_CHOICES)
