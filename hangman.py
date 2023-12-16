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
            for index in indices:
               word_as_list[index] = guess
               word_completion = "".join(word_as_list)
            # Check if word is fully guessed
            if "_" not in word_completion:
               guessed = True
      # Checks if guess is the length of the word
      elif len(guess) == len(word) and guess.isalpha():
         if guess in guessed_words:
            print(Fore.RED + "You already guessed the word", guess)
         # Checks if guessed word is incorrect
         elif guess != word:
            print(Fore.RED + guess, "is not the word.")
            tries_left -= 1
            guessed_words.append(guess)
         else:
            # Correctly guessing whole word
            guessed = True
            word_completion = word
            score += 50  # Add points for guessing the whole word
      else:
         print(Fore.RED + "Not a valid guess.")
         print(hangman_display(tries_left))
         print(word_completion)
         print("\n")
   if guessed:
      print(Fore.GREEN + pyfiglet.figlet_format("You Win!"))
      print(Fore.GREEN + f"Congrats, you guessed the word! Score: {score}")
   else:
      print(Fore.RED + pyfiglet.figlet_format("You Lose!"))
      print(Fore.RED + f"Sorry, you ran out of tries. The word was {word}. Better luck next time! Score: {score}")
               
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
    hangman_display = stages[tries_left]
    return f"tries left: {tries_left}\n{hangman_display}"

def main():
    word = get_random_word()
    play_hangman(word)

    
