from .models import player,team,match,teamrank
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class MatchForm(forms.ModelForm):

    class Meta:
        model = match
        fields = ['team_a','team_b','team_a_goals','team_b_goals','date','time',]
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }

class TeamrankForm(forms.ModelForm):

    class Meta:
        model = teamrank
        fields = []
