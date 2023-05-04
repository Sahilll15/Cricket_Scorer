from rest_framework import serializers
from .models import *

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields =('id','name','captian_name')

class MatchSerializer(serializers.ModelSerializer):
    team_1_name=serializers.CharField(source='team_1.name')        
    team_2_name=serializers.CharField(source='team_2.name') 
    winner_name = serializers.CharField(source='winner.name', allow_null=False)
    Tournament_name=serializers.CharField(source="tournament_name.name")

    class Meta:
            model =Makematch
            fields = ('id','Tournament_name', 'team_1_name', 'team_2_name', 'team_a_score', 'team_b_score','winner_name')

