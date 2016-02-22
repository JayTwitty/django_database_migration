from django.db import models

# Create your models here.

class ClemsonGoogle(models.Model):
    player_name = models.CharField(max_length=30)
    player_position = models.CharField(max_length=10)
    jersey_number = models.IntegerField()
    plays_from_scrimmage = models.IntegerField()
    yards_from_scrimmage = models.IntegerField()
    ave_yards_per_play_from_scrimmage = models.FloatField()
    tds_from_scrimmage = models.IntegerField()