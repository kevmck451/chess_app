# admin.py
from django.contrib import admin
from .models import ChessGame, Move

class ChessGameAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'winner')
    list_filter = ('start_date', 'end_date', 'winner')
    search_fields = ('start_date', 'end_date', 'winner')

class MoveAdmin(admin.ModelAdmin):
    list_display = ('game', 'player', 'move_text', 'timestamp')
    list_filter = ('game', 'player', 'timestamp')
    search_fields = ('move_text',)

# Register your models with the custom admin classes
admin.site.register(ChessGame, ChessGameAdmin)
admin.site.register(Move, MoveAdmin)
