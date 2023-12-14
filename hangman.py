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
    guessed_words = False
    guessed_letters = []
    guessed_words = []
    tries_left = 6
    print(pyfiglet.figlet_format("Hangman"))
    print(word_completion)
    print("\n")


def main():
    word = get_random_word()
    play_hangman(word)

    
