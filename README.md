# PP3-HANGMAN

PP3-HANGMAN is a Python terminal game, which runs on the Code Institute mock terminal on Heroku. Hang-Hangman is a traditional word guessing game.
The user will be given the game rules and a level choice to play the game at Easy or Hard.
The user can try to guess the word by guessing letters, if the letter is wrong a visual of the traditional hangman man will start to display. If the letter is in the word the letter is shown and another guess can be made until either the word gets completed or the user runs out of lives.
The game is for everyone that need a break from real life to collect their thoughts.


* The game can be found [here](https://pp3-hangthe-man.herokuapp.com/).

## How to play
---
- The welcome screen greets the user at a first with a colorfull logo. Rules and options for player to chose to start the game or to choose a difficulty level.
The logo was generated using the Ascii graffiti generator [PatorJK.](https://patorjk.com/software/taag/#p=display&f=Modular&t=HANGMAN)

![Welcomescreen](assets/images/welcomescreen.png)

![Rules and options](assets/images/rules%20and%20options.png)

- If the user chooses option 1. the game starts at a default level of 7 lives and the user will be asked to guess a letter.

![Game Play](assets/images/game_play.png)

- If the user guesses a letter that isn't in the word visuals of the hangman will start building. A varning text in red will inform the user of whats going on. The user looses a life, letter guessed is shown.

![Wrong Letter](assets/images/letter_not_in_word.png)

- If the user guesses the same letter all over again a varning text in red will appeare.

![Same letter](assets/images/same_letter.png)

- If the user guesses something else than a letter a varning text in red will appeare.

![Not a letter](assets/images/not_a_letter.png)

- When the user has runned out of lives before guessing the right word the hangman will appeare together with a text of GameOver in red. The user gets the option to enter Y or N to restart the Game.

![GameOver](assets/images/gameover.png)

- The game will start all over without the welcome screen if the player chooses to enter Y.

![Game Play](assets/images/game_play.png)

- If the user choose to enter N a text will wish the user good bye in green with delay. The player will be taken back to the welcome screen.

![Good Bye](assets/images/good_bye.png)

- If the user chooses option 2 to enter the difficulty level on the welcomescreen a menu will appeare. Here the user can go for Easy (10 lives) or Hard (5 lives). The game starts efter entering the level.

![Difficulty level](assets/images/difficulty_level.png)
