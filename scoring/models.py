from django.db import models
import random


class Tournament(models.Model):
    name = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    location = models.CharField(max_length=200, null=True)
    teams = models.ManyToManyField(
        'Team', blank=True, related_name='tournaments')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200)
    captian_name = models.CharField(max_length=200, null=True)
    captian_email = models.EmailField(null=True)
    captian_phone = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Makematch(models.Model):

    def create_new_ref_number():
        not_unique = True
        while not_unique:
            unique_ref = random.randint(1000000000, 9999999999)
            if not Makematch.objects.filter(match_pin=unique_ref):
                not_unique = False
        return str(unique_ref)
    tournament_name = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team_1 = models.ForeignKey(
        Team, related_name="team_1", on_delete=models.CASCADE)
    team_2 = models.ForeignKey(
        Team, related_name="team_2", on_delete=models.CASCADE)
    match_pin = models.CharField(
        max_length=10, default=create_new_ref_number, null=True, blank=True)
    winner = models.ForeignKey(
        Team, related_name='winner', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.team_1} vs {self.team_2} ({self.tournament_name})"

    def getUrl(self):
        return f'/makematch/{self.id}/scoring/'


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


# class Match(models.Model):
#     tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
#     team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
#     team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
#     winner = models.ForeignKey(Team, related_name='winner', on_delete=models.CASCADE, null=True, blank=True)


# class Innings(models.Model):
#     match = models.ForeignKey(Makematch, on_delete=models.CASCADE)
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     runs = models.IntegerField()
#     wickets = models.IntegerField()
#     overs = models.IntegerField()
#     is_completed = models.BooleanField(default=False)


# class Player(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)


# class BattingScorecard(models.Model):
#     match = models.ForeignKey(Makematch, on_delete=models.CASCADE)
#     player = models.ForeignKey(Player, on_delete=models.CASCADE)
#     runs = models.IntegerField()
#     balls_faced = models.IntegerField()
#     fours = models.IntegerField()
#     sixes = models.IntegerField()
#     is_out = models.BooleanField(default=False)
#     dismissal_type = models.CharField(max_length=100, blank=True)


# class BowlingScorecard(models.Model):
#     innings = models.ForeignKey(Innings, on_delete=models.CASCADE)
#     player = models.ForeignKey(Player, on_delete=models.CASCADE)
#     overs_bowled = models.FloatField()
#     runs_conceded = models.IntegerField()
#     wickets_taken = models.IntegerField()
#     maiden_overs = models.IntegerField()
#     economy_rate = models.FloatField()
