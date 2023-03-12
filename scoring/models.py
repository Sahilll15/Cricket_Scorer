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
    name = models.CharField(max_length=200)
    captain_name = models.CharField(max_length=200,default='')
    contact_number = models.CharField(max_length=20,null=True)
    email = models.EmailField(max_length=200,null=True)
    
    def __str__(self):
        return self.name