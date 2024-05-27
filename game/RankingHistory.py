from django.db import models
from game.models import UserProfile  

class RankingHistory(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    ranking = models.IntegerField()
    date_recorded = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Ranking history for {self.user.user.username} at {self.date_recorded}"
