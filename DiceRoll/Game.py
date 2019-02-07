import time
from Player import Player
from Dice import Dice

class Game(object):
	
	_continue = True
	
	def __init__(self):
		pass

	def play_game(self):
		player = self.get_player_name()
		dice = self.generate_dice()
		dice_roll = dice.roll_dice()
		dice_sum = 0
		print('Rolling the dice...')
		time.sleep(1)
		for roll in dice_roll:
			print(f' The pips come up as : {roll}')
			time.sleep(0.5)
			dice_sum += roll
		print(f'Overall, you rolled {dice_sum}, {player.name}')
		_continue = self.get_continue()
		return _continue
		
			
	def get_continue(self):
		print("Would you like to play again?  'y' or 'n'")
		play_again = input(' > ')
		if play_again == 'y':
			return True
		elif play_again == 'n':
			return False
		else:
			print('u wot m8?')
			return self.get_continue()
		
		
	def generate_dice(self):
		
		while True:
			try:
				print('How many dice shall you roll?')
				how_many_dice = int(input(' > '))
			except ValueError:
				print('You must enter an integer')
				continue
			break
		
		while True:
			try:
				print('What is the lowest die value?')
				min_roll_dice = int(input(' > '))
			except ValueError:
				print('You must enter an integer')
				continue
			break
			
		while True:
			try:
				print('What is the highest die value?')
				max_roll_dice = int(input(' > '))
			except ValueError:
				print("You must enter an integer")
				continue
			if max_roll_dice < min_roll_dice:
				print('Max can\'t be lower than min..')
				continue
			break
		
		new_dice = Dice(how_many_dice, max_roll_dice, min_roll_dice)
		return new_dice			
		
		
	def get_player_name(self):
		print('Welcome to Roll the Dice!')
		print('What is your name?')
		player_name = input(' > ')
		player = Player(player_name)
		return player