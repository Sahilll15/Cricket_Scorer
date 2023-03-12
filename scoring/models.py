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
