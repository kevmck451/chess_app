from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ranking = models.IntegerField(default=1000)  # Initial ranking value
    games_played = models.PositiveIntegerField(default=0)
    games_won = models.PositiveIntegerField(default=0)
    # Add more fields as needed for user statistics

    def __str__(self):
        return self.user.username
