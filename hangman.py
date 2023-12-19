import random
import colorama
import pyfiglet

from words import word_list
from colorama import Fore
# Initialize colorama
colorama.init(autoreset=True)
from pyfiglet import figlet_format

leaderboard = {}  # Initialize an empty leaderboard dictionary

# Gets random word from words.py
def get_word():
    word = random.choice(word_list)
    return word.upper()

def display_leaderboard():
    print("\nLeaderboard:")
    for name, score in sorted(leaderboard.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {score} points")

def play(word):
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
        guess = input(Fore.BLUE + "Please guess a letter or word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(Fore.RED + f"You already guessed the letter {guess}")
            elif guess not in word:
                print(Fore.RED + f"{guess} is not in the word.")
                tries_left -= 1
                guessed_letters.append(guess)
            else:
                print(Fore.GREEN + f"Good job, {guess} is in the word!")
                score += 10
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    word_as_list[index] = guess

                word_completion = "".join(word_as_list)

                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(Fore.RED + f"You already guessed the word {guess}")
            elif guess != word:
                print(Fore.RED + f"{guess} is not the word.")
                tries_left -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
                score += 50
        else:
            print(Fore.RED + "Not a valid guess.")

        print(hangman_display(tries_left))
        print(word_completion)
        print("\n")

    if guessed:
        print(Fore.GREEN + pyfiglet.figlet_format("You Win!"))
        print(Fore.GREEN + f"Congrats, you guessed the word! Score: {score}")
        player_name = input("Enter your name for the leaderboard: ")
        leaderboard[player_name] = score
        display_leaderboard()
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
    # return stages[tries_left]
    hangman_display = stages[tries_left]
    return f"tries left: {tries_left}\n{hangman_display}"

# Starts the game
def main():
    word = get_word()
    play(word)

    while True:
        play_again = input("Would you like to play again? (Y/N) ").upper()

        if play_again == "N" or (play_again != "Y" and play_again != "N"):
            print("Thanks for playing!")
            break

        word = get_word()
        play(word)


if __name__ == "__main__":
    main()