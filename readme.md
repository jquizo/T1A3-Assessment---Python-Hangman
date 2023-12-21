# T1A3 Assessment

### Contents
1. Introduction
2. [References](#r3---references)
2. [Links](#r4---links)
3. [Features](#r6---features)
4. [Implementation Plan](#r7---implementation-plan)
5. [Instructions](#r8---instructions)
6. Dependencies & Libraries

## Hangman - Python Terminal Game
Welcome to Hangman! This game was made using Python and runs on the terminal. The goal of the game is to guess the word one letter at a time, or guess the word before you run out of guesses (6 guesses). You get +10 points for each correct letter guess and +50 points for guessing the word in one go.

## R3 - References
I acknowledge the use of ChatGPT (chat.openai.com) to help produce this application. The prompts used include 

* (ChatGPT, OpenAI, 14th December 2023, Prompt: "I am making a Python hangman game. Can you give me a random unique word list" )

*   Python Software Foundation 2001. PEP 8 - Style Guide for Python Code. Available at: https://peps.python.org/pep-0008/, viewed 20th December 2023.
*  Horton, C. 2017. Hangman Ascii art and wordbank. Available at: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c, viewed 17th December 2023.

## R4 - Links

* [Github page here](https://github.com/jquizo/T1A3-Assessment---Python-Hangman)

## R5 - Style conventions
* This Application follows the PEP 8 – Style Guide for Python Code 
* [Pep 8 Style Guide](https://peps.python.org/pep-0008/)

## R6 - Features
1. **Randomised words** - A random word is pulled from the words.py file using the **random** library. Each game selects a new random word
2. **Fully displayed hangman** - The game calls a function each time a guess is made, and the display hangman function is called to update and display the hangman art depending on how many tries left you have. Making an incorrect guess will reduce the amount of tries you have left and the correct hangman art will be shown. If you guess the word before you run out of your 6 tries you win!
[Hangman art sourced from here](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c)
3. **Leaderboard** - After a game, you get an option to enter your name, and your name and score will be added to the leaderboard. For each correct letter, you get +10 points. If you guess the word in one go, you get +50 points. (Unforunately leaderboards clear after closing the terminal)

## R7 - Implementation Plan
TO DO

## R8 - Instructions
To play this game, you will need **Python** installed. You can get the latest version from [here.](https://www.python.org/)

### Installation steps
1. Clone the repository to your local machine:  

        git clone https://github.com/jquizo/T1A3-Assessment---Python-Hangman

2. Navigate to the project directory

        cd T1A3-Assessment---Python-Hangman

3. Create a virtual environment

        python -m venv venv     

4. Install the required dependencies
    
        pip install -r requirements.txt

        # Dependencies used
        colorama: Used for colored text output.
        pyfiglet: Used for generating ASCII art text.
5. Run hangman

        python hangman.py

You can also run the hangman application on VSCode by opening the hangman.py file on VSCode and running python main.py on the terminal, no installation required. 

### Dependencies & Libraries
* [random](https://docs.python.org/3/library/random.html) - for randomly selecting words
* [colorama](https://pypi.org/project/colorama/) - Used to color feedback messages
* [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) - For ASCII art fonts
