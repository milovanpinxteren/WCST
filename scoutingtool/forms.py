from django import forms


class CritereaSelectorForm(forms.Form):
    player_age_max = forms.IntegerField(required=False)