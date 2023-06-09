from django import forms
from . models import Tournament, Team,Player


class TournamentForms(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'start_date', 'end_date', 'location']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ['name', 'captian_name' ]

    

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name' , 'team','role']

# from django import forms

# class BattingScorecardForm(forms.ModelForm):
#     class Meta:
#         model = BattingScorecard
#         fields = ['player', 'runs', 'balls_faced', 'fours', 'sixes', 'is_out', 'dismissal_type']

# class BowlingScorecardForm(forms.ModelForm):
#     class Meta:
#         model = BowlingScorecard
#         fields = ['player', 'overs_bowled', 'runs_conceded', 'wickets_taken', 'maiden_overs', 'economy_rate']
