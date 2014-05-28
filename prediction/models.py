from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=3)
    def __unicode__(self):
        return self.name

class Match(models.Model):
    datetime = models.DateTimeField('matche date')
    home_team = models.ForeignKey(Team, related_name='home_team_id')
    away_team = models.ForeignKey(Team, related_name='away_team_id')
    game_week = models.IntegerField()
    def __unidoe__(self):
        return self.home_team_name + ' vs ' + self.away_team.name
    class Meta:
        verbose_name_plural = "Matches"

class Result(models.Model):
    match = models.ForeignKey(Match)
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
    def __unicode__(self):
        return self.match.home_team.name + \
                ': ' + str(self.home_goals) + \
                ' ' + self.match.away_team.name + \
                ': ' + str(self.away_goals)

class Prediction(models.Model):
    match = models.ForeignKey(Match)
    user = models.ForeignKey(User)
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
