"""
Libraries and imports
"""

import random
import colorama
import os
from words import hidden_words
from graphics import welcome, win, loose, tries_left, god_bye
from colorama import Fore
from time import sleep

colorama.init(autoreset=True)

def welcome_screen():
    """
    Logo, rules and options for player to begin the game
    or select the difficulty level.
    """
    print(Fore.YELLOW + welcome)
    print("Welcome dear player! It's time to try to stay alive...\n")
    sleep(1)
    print(
        "Please read the following instructions\n"
        "to find your way to and trough the game.\n"
    )
    sleep(1)
    print(
        "You can choose your difficulty level before entering the game.\n"
        "Easy level has 10 lives and hard level has 5 lives.\n"
        )
    sleep(1)
    print(
        "Then try and guess the secret word one letter at a time\n"
        "before you're out of lives.\n"
    )
    sleep(1)
    print(
        "For each wrong guessed letter you lose one life\n"
        "and your gallows gets built more until you dangle.\n"
    )
    sleep(1)
    print(
        "If you want to play again, simply restart the game\n"
        "by entering Y or enter N to exit the game.\n"
    )
    print("Press " + "1" + " to start game")
    print("Press " + "2" + " to enter the difficulty level")

    opt = False
    while not opt:
        settings = input("\n")
        if settings == "1":
            opt = True
            clean_screen()
            difficulty_l = "default"
            return difficulty_l

        elif settings == "2":
            opt = True
            clean_screen()

        else:
            print("\n")
            print(f"{Fore.RED}Please enter 1 or 2 to make your choice")
            clean_screen()

def choose_difficulty():
    """
    This is where the player gets to chose difficulty level.
    """
    print("\n")
    print("Select Difficulty level\n")
    print("Press " + "E" + " for Easy")
    print("Press " + "H" + " for Hard")

    level = False
    while not level:
        difficulty = input("\n").upper()
        if difficulty == "E":
            level = True
            clean_screen()
            total_lives = 10
            return total_lives
        elif difficulty == "H":
            level = True
            clean_screen()
            total_lives = 5
            return total_lives
        else:
            print("\n Please enter E or H to make your choice")