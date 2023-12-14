import random
import colorama 

from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from words import word_list


def get_random_word():
    word = random.choice(word_list)
    return word.upper()

