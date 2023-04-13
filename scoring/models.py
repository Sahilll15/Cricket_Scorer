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
    name = models.CharField(max_length=200,unique=True)
    captian_name = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.captian_name:
            captain = Player(name=self.captian_name, team=self, captain=True)
            captain.save()


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
    team_2= models.ForeignKey(
        Team, related_name="team_2", on_delete=models.CASCADE)
    team_a_score = models.IntegerField(default=0)
    team_b_score = models.IntegerField(default=0)
    # match_pin = models.CharField(
    #     max_length=10, default=create_new_ref_number, null=True, blank=True)
    winner = models.ForeignKey(
        Team, related_name='winner', on_delete=models.CASCADE, null=True, blank=True)
    
      

    def __str__(self):
        return f"{self.team_1} vs {self.team_2} ({self.tournament_name})"

    def getUrl(self):
        return f'/makematch/{self.id}/scoring/'


class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    captain = models.BooleanField(default=False)
    

    class Meta:
        # Add unique constraint that spans across the name and team fields
        unique_together = ('name', 'team',)


    def __str__(self):
        return f'{self.name}'


class Batter(models.Model):
    match = models.ForeignKey(Makematch, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    runs = models.IntegerField(default=0)
    balls_faced = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)
    out = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.player} ({self.runs} runs)'


class Bowler(models.Model):
    match = models.ForeignKey(Makematch, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    overs = models.DecimalField(max_digits=3, decimal_places=1)
    runs = models.IntegerField()
    wickets = models.IntegerField()

    def __str__(self):
        return self.player.name
