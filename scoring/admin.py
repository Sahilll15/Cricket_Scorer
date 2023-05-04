from django.contrib import admin
from .models import *


admin.site.register(Tournament)



# admin.site.register(Batter)
# admin.site.register(Bowler)



class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'role', 'captain')
    list_filter = ('team', 'role', 'captain')
    ordering = ('team',)


class TeamAdmin(admin.ModelAdmin):
    list_display=['name']
    

admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)

class MakematchAdmin(admin.ModelAdmin):
    list_display=['tournament_name','overs','winner','team_1','team_2','team_a_score','team_b_score']
    ordering=['-winner','-team_a_score']

admin.site.register(Makematch,MakematchAdmin)


