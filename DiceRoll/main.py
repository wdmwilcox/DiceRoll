from Game import Game


def main():

	loop_game = True
	while loop_game is True:
		new_game = Game()
		loop_game = new_game.play_game()
	exit(0)


if __name__ == "__main__":
	main()

	

