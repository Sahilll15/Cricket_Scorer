from django import forms
from . models import Tournament,Team

class TournamentForms(forms.ModelForm):
    teams=forms.ModelMultipleChoiceField(queryset=Team.objects.all(),required=False,widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Tournament
        fields = ['name',  'start_date', 'end_date', 'location']

class TeamForms(forms.ModelForm):
    class Meta:
        model=Team
        fields=['name','captain_name']
        