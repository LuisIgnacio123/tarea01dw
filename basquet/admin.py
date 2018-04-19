from django.contrib import admin
from .models import *


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	list_display = ('code_team','logo_team', 'name_team',)
	list_filter = ('code_team', 'name_team',)
	search_fields = ('name_team', 'code_team',)
	


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	list_display = ('name_player','photo', 'nickname_player', 'code_team')
	search_fields = ('name_player', 'nickname_player', 'rut_player')
	list_filter = ('code_team', 'birth_date',)
		
@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	list_display = ('name_coach', 'nickname_coach', 'code_team',)
	search_fields = ('name_coach', 'code_team')
	
		
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	list_display = ('name_game',)
	search_fields = ('name_game',)
	
