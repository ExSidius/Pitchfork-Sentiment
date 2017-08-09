
def clear():
	import os
	os.system('clear')

def intro():
	print("\nHey, it's Jackie!\n")

def loop():
	while True:

		print('> ', end='', flush=True)
		command=input().lower()		

		# print('You wrote ' + command + '.')

		if 'exit' in command or 'quit' in command:
			clear()
			exit()

def main():

	clear()

	intro()

	loop()

	exit()

if __name__ == "__main__":
    main()