from django.db import models

class Team(models.Model):
	"""docstring for ClassName"""
	name_team = models.CharField(max_length=200)
	description = models.TextField()
	logo_team = models.ImageField()
	code_team = models.Interger()

	def __str__(self):
		return self.name


class Player(models.Model):
	"""docstring for ClassName"""
	name_player = models.CharField(max_length=200)
	nickname = models.CharField(max_length=100)
	birth_date = models.DateTime()
	years = models.Interger()
	rut = models.CharField()
	email = models.CharField()
	height = models.Interger()
	weight = models..Interger()
	photo = models.ImageField()
	game_position = ('Base','base',)
	code_team = models.ForeignKey('Team',on_delete=models.CASCADE)	

	def __str__(self):
		return self.name



class Coach(models.Model):
	"""docstring for ClassName"""
	name_coach = models.CharField(max_length=200)
	years = models.Interger()
	email = models.CharField()
	rut = models.CharField()
	nickname = CharField(max_length=100)
	code_team = models.ForeignKey('Team',on_delete=CASCADE)

	def __str__(self):
		return self.name

class Game(models.Model):
	"""docstring for ClassName"""
	name_game = models.CharField(max_length=200)

	def __str__(self):
		return self.name

		
		
		
