# PP3-HANGMAN

PP3-HANGMAN is a Python terminal game, which runs on the Code Institute mock terminal on Heroku. Hang-Hangman is a traditional word guessing game and is for everyone that need a break from real life to collect their thoughts.


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

## Flowchart
---
This was my initial plan for the game. Some of the futures have changed as I developed the game.
![Flowchart](assets/images/)

## Features
---
- The user plays against the computer.
- The computer accepts user input and gives responsive feedback.
- Random word generator
- The word is encrypted, so the user cannot see the word straight away, only the length appeare.
- If the user guesses wrong letter the guessed letter will be displayed througout the whole game.
- If the user guesses right letter the letter will be displayed in the encrypted word.
- Validation and error handling for duplicate enteries, special characters and numbers.
- Messages to the user are colored in red to stick out from the screen.

## Testing
---
- Family and friends tested for functionality
- Tested for all scenarios with incorrect guesses.
- Tested for all scenarios with successful guess.
- Tested for all scenarios with moore than one letter and special characters.
- Tested for empty input. 

### Code validation
PEP8 validated with no errors.

## Bugs
- Some lines are to long and there where multiple whitespaces in the kode. PEP8 kept tracked on these during the build up and are fixed.
- Thoroughout testing there where a lack of spaces between lines, that was fixed with "\n".
- After deploying the game I realized that the user couldn't win the game. This was.........

## Technologies Used
---
### Languages
- [Python:](https://www.python.org/) Python was the language beeing used for the whole project.
- [Markdown:](https://www.markdownguide.org/basic-syntax/) Markdown language was used for writing the README.md/

### Librarys
- random to select a random word.
- os to clear the screen.
- colorama to add color to text and images.

 
### Environment
- [GitHub:](https://github.com/) hosted the code.
- [GitPod:](https://www.gitpod.io/?utm_source=googleads&utm_medium=search&utm_campaign=dynamic_search_ads&utm_id=16501579379&utm_content=dsa&gclid=EAIaIQobChMIn6TCrsyA-wIVDNPtCh319wDpEAAYASAAEgKK2vD_BwE) was used to write the code.
- [Heroku:](https://id.heroku.com/login) was the cloud hosting platform used for deploying this project.
 
### Other
- [Graffiti:](http://patorjk.com/software/taag/#p=display&h=1&v=2&f=Pawp&t=Hangman) was used for the large text images in the game.

## Deployment
---
The project was deployed using Code Institutes mock terminal for Heroku. 

- Steps to deploy:
  - Fork or clone this repository.
  - Ensure the Procfile is in place.
  - requirements.txt can be left empty as this project does not use any external libraries. 
  - Create a new app in [Heroku](https://dashboard.heroku.com/apps).
  - Select "New" and "Create new app".
  - Name the new app and click "Create new app".
  - In "Settings" select "BuildPack" and select Python and Node.js. (Python must be at the top of the list).
  - Whilst still in "Settings", click "Reveal Config Vars" and input the folloing. KEY: PORT, VALUE: 8000. Nothing else is needed here as this project does not have any sensitive files.
  - Click on "Deploy" and select your deploy method and repository.
  - Click "Connect" on selected repository. 
  - Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section. 
  - Heroku will now deploy the site.

## Credits
- [YouTube](https://www.youtube.com/watch?v=cJJTnI22IF8&t=2s&ab_channel=KylieYing) - for inspiration 
- [YouTube](https://www.youtube.com/watch?v=m4nEnsavl6w) - for inspiration
- [YouTube](https://www.youtube.com/watch?v=3_CX0aD9Fdg&t=272s) - for inspiration
- I've used several more youtube videos to get the hang of how to create a Hangman game in python. The above videos are the ones I took most inspiration from.








