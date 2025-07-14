import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
end_of_game = False
#Testing code
print(f'Pssst, the solution is {chosen_word}.')
while not end_of_game:
	guess = input("what word do you guess?").lower()
	Display = []
	for _ in chosen_word:
		Display += "_"

	for position in range(len(chosen_word)):
		letter = chosen_word[position]
		print(f"Current position: {position}\n Current letter:{letter}\n Guessed letter:{guess}")
		if letter == guess:
			Display[position] = letter
			 
	print(Display)
	
if "_" not in Display:
	end_of_game = True
	print("You win")
				
