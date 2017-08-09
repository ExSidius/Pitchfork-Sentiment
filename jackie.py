
def clear():
	import os
	os.system('clear')

def intro():
	print("\nHey, it's Jackie!\n")


def get_blocks(game):



def solve(file):
	import pandas as pd
	import numpy as np

	df = pd.read_csv(file, header=None)
	print(df.shape)

	game = df.values

	rows = game
	columns = np.transpose(game)
	blocks = get_blocks(game)


def loop():
	while True:

		print('> ', end='', flush=True)
		command=input().lower()		

		# print('You wrote ' + command + '.')

		if 'exit' in command or 'quit' in command:
			clear()
			exit()

		if 'sudoku' in command:
			solve('game.csv')

def main():

	clear()

	intro()

	loop()

	exit()

if __name__ == "__main__":
    main()