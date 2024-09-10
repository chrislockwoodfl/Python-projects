# Hangman game by Chris Lockwood

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel", "beagle", "elephant", "tiger", "horse", "donkey", "penguin", "flamingo", "orangutan", "gorilla"]


chosen_word = random.choice(word_list)
#print(chosen_word)
lives = 6

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

print("Let's play Hangman. I'm thinking of a word. Guess the letters until you have the entire word. You have 6 guesses left.")
while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    # If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    if guess not in chosen_word:
        lives -= 1

    #  print the hangman graphic that matches number of lives left
    print(stages[lives])

    # print word in progress
    print(display + "\n")

    if lives == 0:
        game_over = True
        print("You ran out of guesses. You lose. The word was", chosen_word + ".")
    elif "_" not in display:
        game_over = True
        print("You win!")

