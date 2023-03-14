from django import forms
from . models import Tournament, Team


class TournamentForms(forms.ModelForm):
    # teams=forms.ModelMultipleChoiceField(queryset=Team.objects.all(),required=False,widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Tournament
        fields = ['name',  'start_date', 'end_date', 'location']


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ['name', 'captian_name', 'captian_email', 'captian_phone']


# from django import forms

# class BattingScorecardForm(forms.ModelForm):
#     class Meta:
#         model = BattingScorecard
#         fields = ['player', 'runs', 'balls_faced', 'fours', 'sixes', 'is_out', 'dismissal_type']

# class BowlingScorecardForm(forms.ModelForm):
#     class Meta:
#         model = BowlingScorecard
#         fields = ['player', 'overs_bowled', 'runs_conceded', 'wickets_taken', 'maiden_overs', 'economy_rate']
