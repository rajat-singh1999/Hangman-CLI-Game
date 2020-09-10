import random as ran

def hangman(n):
	if n==0:
		print("---------")
		print("         ")
		print("         ")
		print("         ")
	elif n==1:
		print("---------")
		print("  o      ")
		print("         ")
		print("         ")
	elif n==2:
		print("---------")
		print("  o      ")
		print("  |      ")
		print("         ")
	elif n==3:
		print("---------")
		print("  o      ")
		print(" /|      ")
		print("         ")
	elif n==4:
		print("---------")
		print("  o      ")
		print(" /|\     ")
		print("         ")
	elif n==5:
		print("---------")
		print("  o      ")
		print(" /|\     ")
		print("   \     ")
	elif n==6:
		print("---------")
		print("  o      ")
		print(" /|\     ")
		print(" / \     ")
	elif n==7:
		print("---------")
		print("  o   |  ")
		print(" /|\     ")
		print(" / \     ")
	elif n==8:
		print("---------")
		print("  o  _|  ")
		print(" /|\     ")
		print(" / \     ")

	else:
		print("---------")
		print("  o_|    ")
		print(" /|\     ")
		print(" / \     ")

words = ["water", "paper", "computer", "table", "glass", "mouse", "lion", "koala", "mask", "sanitizer"]

print("Welcome to the Hangman CLI game!")
print("Let's start!")

rand_word = ran.choice(words)
dashes = len(rand_word)*"_"
clone_word = rand_word

print(f"Guess the word: {dashes}")
inp = input("Give a letter: ")
count = 0

while True:
	if inp in rand_word and inp is not "":
		hangman(count)
		print(f"Correct letter!")
		
		ind = rand_word.index(inp)
		dashes = dashes[:ind] + inp + dashes[ind + 1:]
		rand_word = rand_word[:ind] + "_" + rand_word[ind + 1:]

		print(f"Word: {dashes}")
		if rand_word != "_"*len(clone_word) and count < 9:
			inp = input("Give a letter: ")
		else:
			break

	else:
		count = count + 1
		hangman(count)
		print(f"Not a Correct letter!")
		print(f"Word: {dashes}")
		if rand_word != "_"*len(clone_word) and count < 9:
			inp = input("Give a letter: ")
		else:
			break

if rand_word != "_"*len(clone_word):
	print(f"You loose! The word is {clone_word}.")
else:
	print(f"You Won! The word is {clone_word}")







	

