from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1_matches')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2_matches')
    pin = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} ({self.pin})"


