from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Team(models.Model):
    name = models.CharField(max_length=50, null=False)
    points = models.IntegerField(null=True)


class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    number = models.IntegerField(null=True)

class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_team', on_delete=models.SET_NULL, null=True, blank=True)
    away_team = models.ForeignKey(Team, related_name='away_team', on_delete=models.SET_NULL, null=True, blank=True)
    home_score = models.IntegerField(null=True)
    away_score = models.IntegerField(null=True)

class Comment(models.Model):
    text = models.CharField(max_length=256, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    match = models.ForeignKey(Match, on_delete=models.SET_NULL, null=True, blank=True)

