from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Permission, User
from django.utils.text import slugify
from django_resized import ResizedImageField
from django.contrib.auth.models import UserManager
from django.db.models import Sum
from django.core.validators import MaxValueValidator
from django.conf import settings
import random


class team(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    passcode = models.CharField(max_length=10, blank=True, null=True)
    teamname = models.CharField(max_length=100, blank=True, null=True,default="Team name "+ str(random.randint(10,1000)))
    logo = ResizedImageField(size=[300, 300], crop=['middle', 'center'], quality=100, blank=True,default="soccer_logo.jpeg")
    coverpic = ResizedImageField(size=[800, 350], crop=['middle', 'center'], quality=100, null=True,blank=True,default='soccer.jpeg')
    teamquotes = models.CharField(max_length=20000, default='hey!I am ready for the battle', null=True, blank=True)
    teamcontact = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.teamname


class player(models.Model):
    teamname = models.ForeignKey(team, on_delete=models.CASCADE, related_name="players")
    player = models.CharField(max_length=100, blank=True, null=True)
    playerpasscode = models.IntegerField(default='0000', blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    facebookurl = models.URLField(default='https://www.facebook.com', blank=True, null=True)
    instaurl = models.URLField(default='https://www.instagram.com', blank=True, null=True)
    position = models.CharField(default='unknown', max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, default='hey! i am a battle soccer player', blank=True, null=True)
    pic = ResizedImageField(size=[300, 300], crop=['middle', 'center'], quality=100,default="soccer_player.jpeg")
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="votes")
  

class match(models.Model):
    team_a= models.ForeignKey(team,default=1, on_delete=models.CASCADE,related_name='belongs')
    team_b= models.ForeignKey(team,default=1, on_delete=models.CASCADE)
    team_a_goals=models.IntegerField()
    team_b_goals=models.IntegerField()
    date=models.DateField(blank=True, null=True)
    time=models.TimeField(blank=True, null=True)
    winner=models.CharField(max_length=200)


    def __str__(self):
        return self.team_a



class teamrank(models.Model):
    teamown = models.OneToOneField(team,default=1, on_delete=models.CASCADE)
    teamname=models.CharField(max_length=200,default=1)
    teamgoals=models.IntegerField()
    matchs_played=models.IntegerField()
    match_won=models.IntegerField()
    match_lost=models.IntegerField()

    def __str__(self):
        return self.teamname

class highlights(models.Model):
    teamname= models.ForeignKey(team,default=None, on_delete=models.CASCADE,related_name="videos")
    highlight=models.URLField();
  

    def __str__(self):
        return str(self.teamname)

class contestteam(models.Model):
    teamown = models.OneToOneField(team,default=1, on_delete=models.CASCADE)
    teamcontact = models.IntegerField(blank=True,null=True)
    contactname=models.CharField(max_length=200,default=1)


    def __str__(self):
        return self.teamown