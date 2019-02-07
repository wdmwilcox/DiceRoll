import random

class Dice(object):
	
	def __init__(self, how_many, max_roll, min_roll):
		self.how_many = how_many
		self.max_roll = max_roll
		self.min_roll = min_roll
		
	def roll_dice(self):
		dice_numbers = []
		for die in range(self.how_many):
			dice_numbers.append(random.randint(self.min_roll, self.max_roll))
		return dice_numbers