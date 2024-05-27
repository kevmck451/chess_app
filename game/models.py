# models.py
from django.db import models

class ChessGame(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    winner = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Chess Game #{self.pk}"

class Move(models.Model):
    game = models.ForeignKey(ChessGame, on_delete=models.CASCADE)
    player = models.CharField(max_length=255)
    move_text = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Move #{self.pk} in Game #{self.game.pk}"
