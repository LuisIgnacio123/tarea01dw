from django.db import models

class Team(models.Model):
	"""docstring for ClassName"""
	name_team = models.CharField(max_length=200)
	description = models.TextField()
	logo_team = models.ImageField()
	code_team = models.IntegerField()

	def __str__(self):
		return self.name


class Player(models.Model):
	"""docstring for ClassName"""
	name_player = models.CharField(max_length=200)
	nickname_player = models.CharField(max_length=100)
	birth_date = models.DateTimeField()
	years = models.IntegerField()
	rut_player = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	height = models.IntegerField()
	weight = models.IntegerField()
	photo = models.ImageField()
	game_position = ('Base','base',)
	code_team = models.ForeignKey(Team, on_delete=models.CASCADE)	

	def __str__(self):
		return self.name



class Coach(models.Model):
	"""docstring for ClassName"""
	name_coach = models.CharField(max_length=200)
	years = models.IntegerField()
	email = models.CharField(max_length=100)
	rut_coach = models.CharField(max_length=100)
	nickname_coach = models.CharField(max_length=100)
	code_team = models.ForeignKey(Team,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Game(models.Model):
	"""docstring for ClassName"""
	name_game = models.CharField(max_length=200)

	def __str__(self):
		return self.name

		
		
		
