from django.db import models


class Tournament(models.Model):
    name=models.CharField(max_length=200,null=True)
    start_date=models.DateTimeField(null=True)
    end_date=models.DateTimeField(null=True)
    location=models.CharField(max_length=200,null=True)
    teams = models.ManyToManyField('Team', blank=True, related_name='tournaments')

    def __str__(self) :
        return self.name

class Team(models.Model):
    name=models.CharField(max_length=200)
    captian_name=models.CharField(max_length=200,null=True)
    captian_email=models.EmailField(null=True)
    captian_phone=models.IntegerField(null=True)

    def __str__(self) :
        return self.name
    

class Makematch(models.Model):
    tournament_name=models.ForeignKey(Tournament,on_delete=models.CASCADE)
    team_1=models.ForeignKey(Team,related_name="team_1",on_delete=models.CASCADE)
    team_2=models.ForeignKey(Team,related_name="team_2",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team_1} vs {self.team_2} ({self.tournament_name})"



