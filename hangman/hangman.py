# Hangman game by Chris Lockwood

import random

# import word list and hangman art
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)
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
guesses = []

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

    # If guess is not a letter in the chosen_word, Then reduce 'lives' by 1,
    # unless player has already guessed that letter
    if guess not in chosen_word and guess not in guesses:
        lives -= 1
        print("You guessed", guess + ". That's not in the word.")
    else:
        print("You already guessed", guess + ".")

    print("You have", lives, "guesses left.")
    guesses.append(guess)

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