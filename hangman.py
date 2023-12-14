import random
import colorama 
import pyfiglet

from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from words import word_list
from pyfiglet import figlet_format


def get_random_word():
    word = random.choice(word_list)
    return word.upper()


def play_hangman(word):
   word_completion = "_" * len(word)
   guessed = False
   guessed_letters = []
   guessed_words = []
   tries_left = 6
   score = 0  
   print(pyfiglet.figlet_format("Hangman"))
   print("+10 score for each LETTER guessed. 50 points for guessing the correct word!!")
   print(word_completion)
   print(hangman_display(tries_left))
   print("\n")
   # Initialise game loop
   while not guessed and tries_left > 0:
      # Get user input
      guess = input(Fore.BLUE + "Please guess a letter or word: ").upper()
      # Checks if guess is a single letter
      if len(guess) == 1 and guess.isalpha():
      # Checks if the letter has already been guessed
         if guess in guessed_letters:
            print(Fore.RED + "You already guessed this letter", guess)
      # Check if the letter is not in the word
      elif guess not in word:
         print(Fore.RED + guess, Fore.RED + "is not in the word.")
         tries_left -= 1
         guessed_letters.append(guess)
      else: 
      # Correct letter guess
         print(Fore.GREEN + "Good job,", Fore.GREEN + guess, Fore.GREEN + "is in the word!")
         score += 10  # Add points for each correct letter
         guessed_letters.append(guess)
         word_as_list = list(word_completion)
         indices = [i for i, letter in enumerate(word) if letter == guess]
         # Update word_completion with the correctly guessed letter
         

def hangman_display(tries_left):
    stages = [  # head, torso, both arms, and both legs
                """
                   ========
                   |      |
                   |      O      OUCH!
                   |     \\|/   
                   |      |
                   |     / \\
                   ========
                """,
                # head, torso, both arms, and one leg
                """
                   ========
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   ========
                """,
                # head, torso, and both arms
                """
                   ========
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   ========
                """,
                # head, torso, and one arm
                """
                   ========
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   ========
                """,
                # head and torso
                """
                   ========
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   ========
                """,
                # head
                """
                   ========
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   ========
                """,
                # initial empty state
                """
                   ========
                   |      |
                   |      
                   |    
                   |      
                   |     
                   ========
                """
    ]


def main():
    word = get_random_word()
    play_hangman(word)

    
