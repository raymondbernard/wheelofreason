# Wheel of Reason for Language Models

Welcome to Wheel of Reason, an intriguing and challenging game specifically designed for large language models, often employed through a front-end interface such as ChatGPT, bard.google.com , Claude v2 etc. This game tests the model's reasoning skills and vocabulary comprehension.


### What we are measuring?
The "Wheel of Reason" game provides a way to measure several aspects of an AI's capabilities:

1. **Natural Language Processing (NLP):** The AI needs to understand the inputs provided by the user, interpret the instructions of the game, and communicate its decisions effectively.

2. **Decision Making:** The AI must choose the best actions to take at each stage of the game (whether to spin the wheel, buy a vowel, or solve the puzzle). This involves strategic thinking and making calculated risks.

3. **Problem Solving:** Solving the puzzle requires identifying patterns, making educated guesses, and continually updating information based on new inputs (like correctly guessed letters).

4. **Memory and Learning:** The AI should remember the letters it has already guessed and learn from unsuccessful attempts to improve future performance.

5. **Reasoning:** The AI needs to reason about the current state of the game and make informed decisions. This could involve statistical reasoning (e.g., considering the frequency of different letters in the English language) and logic.

6. **Gameplay:** Beyond the cognitive skills required to play the game, the AI is also measured on its ability to follow the rules of the game and interact with the game's infrastructure (e.g., spinning the wheel, buying vowels, keeping track of its score).

In sum, the "Wheel of Reason" game measures an AI's ability to understand and generate natural language, remember and learn from past events, reason logically and statistically, and interact with a rule-based system.


Evaluating AI performance in a game context such as the "Wheel of Reason" involves identifying the key skills necessary for the game and defining metrics for each skill. Here are some suggested metrics:

1. **Game Win Ratio:** How often does the AI win the game? This is the most straightforward metric, but it doesn't tell you much about why the AI is winning or losing.

2. **Guess Accuracy:** What percentage of the AI's letter guesses are correct? This metric assesses the AI's language understanding and pattern recognition skills.

3. **Efficiency:** How many turns does the AI need to solve a puzzle on average? This measures the AI's decision-making and problem-solving efficiency.

4. **Vowel Buying Strategy:** How effective is the AI's strategy of buying vowels (i.e., does buying vowels typically lead to a faster solution or not)? This can be evaluated by comparing the win ratio or efficiency of games where the AI bought vowels versus games where it didn't.

5. **Score:** What's the average score of the AI across games? This accounts for both puzzle-solving and other strategic aspects of the game, such as landing on high-value spins or hitting penalties.

6. **Use of Information:** How well does the AI use the information available to it? For instance, does it avoid guessing letters that have already been guessed or revealed in the puzzle? Does it use frequency analysis (some letters are more common in English words than others) to guide its guesses?

7. **Error Rate:** Measure the number or percentage of errors made during the game. An error could be defined as an incorrect guess or a decision that goes against optimal gameplay strategies.

Once you have these metrics, you could present them to a data scientist as a summary statistics table or a series of histograms or box plots. You could also examine the correlations between different metrics to explore which skills are most closely linked to success in the game. Additionally, a time-series analysis could be conducted to understand how the AI's performance evolves over multiple games, measuring the AI's learning capability. 

Also, consider using A/B testing for different strategies, for instance comparing versions of the AI with and without the use of certain strategies or capabilities. 

Finally, it's important to have a baseline for comparison. This could be the performance of a random guessing strategy, human performance, or the performance of a previous version of the AI. The goal is to measure the AI's performance relative to this baseline, providing a more meaningful context for your metrics.


Sure, here's a way to quantify the measures for each category:

1. **Game Win Ratio:** This could be calculated as:

    `Win Ratio = (Number of games won / Total number of games played) * 100%`

2. **Guess Accuracy:** You could measure this as:

    `Guess Accuracy = (Number of correct guesses / Total number of guesses) * 100%`

3. **Efficiency:** This can be represented as:

    `Efficiency = Total number of turns / Number of games won`

    Lower numbers indicate higher efficiency, as it means fewer turns were needed to win each game.

4. **Vowel Buying Strategy:** To evaluate this, you could compare the win ratios or efficiencies when using the strategy vs. not:

    `Effectiveness of Vowel Buying Strategy = (Win Ratio/Efficiency with vowel buying) - (Win Ratio/Efficiency without vowel buying)`

5. **Score:** This is typically provided by the game itself but can be averaged over games:

    `Average Score = Total score across all games / Total number of games played`

6. **Use of Information:** You could calculate an "Information Use Score" based on a list of desirable actions that reflect good use of information. For instance, for each desirable action the AI takes (e.g., not guessing letters that have already been guessed), you could add a point, and for each undesirable action (e.g., guessing a letter that has already been revealed), you could subtract a point:

    `Information Use Score = Number of desirable actions - Number of undesirable actions`

    You could also standardize this score by the number of turns or the number of opportunities the AI had to use information:

    `Standardized Information Use Score = Information Use Score / Total number of turns or opportunities`

7. **Error Rate:** This could be measured as:

    `Error Rate = (Number of incorrect guesses or suboptimal decisions / Total number of decisions or guesses) * 100%`

These measures provide a comprehensive overview of an AI's performance in the Wheel of Reason game. They cover a range of skills and strategies, and by analyzing them together, you can gain a deep understanding of the AI's strengths and weaknesses.

## Game Overview

Wheel of Reason is more than just a game - it's a tool to measure and test the reasoning capabilities and language understanding of large language models. By playing Wheel of Reason, developers and researchers can assess a model's ability to guess, reason, and solve language-based puzzles.

## Rules

1. The game is played in a series of turns. In each turn, a language model can select from three different actions:

    - **Spin the Wheel**: The wheel is divided into different segments, each depicting various amounts of points, a bankrupt slot, or a lose-a-turn slot.
    
    - **Buy a Vowel**: For a flat rate of 250 points, a language model can choose to guess a vowel that it believes might be present in the phrase.
    
    - **Solve the Puzzle**: If the language model believes it has cracked the code, it can take a shot at solving the puzzle. If its answer is correct, it emerges victorious!
  
2. When the language model spins the wheel and lands on a points segment, it can guess a consonant. If the consonant is in the phrase, it earns the points depicted on the wheel times the number of times the consonant appears in the phrase. If the consonant is not in the phrase, its turn ends.

3. If the language model has sufficient points, it can opt to buy a vowel instead of spinning the wheel. This comes with a fixed cost of 250 points. If the vowel is present in the phrase, it retains its turn. If the vowel is not in the phrase, its turn ends.

4. If the language model believes it knows the phrase, it can attempt to solve the puzzle. If its answer is correct, it wins the game. If its answer is incorrect, its turn ends.

5. The game concludes when a language model successfully solves the puzzle. The model that solves the puzzle is deemed the winner.

## Objective

The goal of Wheel of Reason is to provide an engaging platform to test the reasoning and language understanding of large language models. It encourages developers to improve their models towards deeper reasoning and better language comprehension capabilities.

Ready to play? Let's get back to the game!


# Wheel of Reason Game: Installation and Usage Instructions

## Requirements
- Python 3.x (preferably Python 3.8 or newer)
- JSON files: 'wheel.json' and 'phrases.json' (included in the source files)

## Installation

1. **Download the Source Code**

    Download the Python script and the required JSON files.

2. **Check Python Installation**

    Verify that Python 3.x is installed on your system by running the following command in your command line:

    ```sh
    python --version
    ```

    You should see output similar to `Python 3.x.y`, where `x` and `y` are the major and minor version numbers, respectively. If Python is not installed or the version is incorrect, you will need to [install or update Python](https://www.python.org/downloads/) on your system.

3. **Prepare JSON files**

    Place 'wheel.json' and 'phrases.json' files in the same directory as the Python script.

## Running the Game

1. **Navigate to the Script's Directory**

    Open a command line interface and navigate to the directory containing the Python script and JSON files.

    ```sh
    cd path/to/directory
    ```

2. **Run the Script**

    Run the Python script:

    ```sh
    python game_script.py
    ```

    Replace `game_script.py` with the name of your Python script if it's different.

3. **Follow the In-Game Prompts**

    Once the game has started, simply follow the on-screen prompts. The game will instruct you when to spin the wheel, guess a letter, or solve the puzzle.

    When prompted, you can input '4' to display a help message that outlines the game rules and mechanics.
Sure, I can help you with that. Here is an example of how you can update the `Readme.md` file to reflect the changes you've mentioned:

---

In the most recent version of the game, we've added some new functionalities:

1. **User Addition from Command Line**: Now you can add players directly from the command line. This makes it easier to get started with a new game.

2. **Randomized Player Order**: We've added a bit more unpredictability to our game. Now, the order of players is randomized at the start of each game.

3. **Puzzle-Solving Winner**: The game has been updated so that the winner is the player who solves the puzzle. This encourages strategic thinking and problem-solving.

4. **Enhanced Logging**: Game statistics are now logged both to our log files and printed on the console. This allows for easier tracking of game progress and statistics.

## Getting Started

To add users from the command line, use the following command:

```bash
python wheelofreason.py --add-user <username>
```

Replace `<username>` with the name of the user you want to add.

## Game Play

At the start of the game, the order of players is randomized. Players take turns spinning the wheel, guessing letters, and attempting to solve the puzzle. The player who solves the puzzle is declared the winner.

---

Please replace any placeholder text (like `<username>`) with the actual commands or variables used in your code. Also, feel free to modify or extend this template to best fit your project and its requirements.
## Notes

This game is currently interactive and requires manual user input for all player actions. The players' names are hardcoded and each player's actions are performed by user input in the console.

To run the game in a non-interactive environment, you would need to modify the source code to provide player actions programmatically or through some other interface.


## Future Improvements

1. **Convert the Python Script to a Jupyter Notebook**

    Jupyter Notebook could be used to transform this script into an interactive demonstration or tutorial. The code can be divided into separate cells that can be run independently, allowing users to experiment with different parts of the game in isolation.

    Here's how you could do it:

    - Install Jupyter Notebook: Use pip to install Jupyter:
      ```sh
      pip install notebook
      ```
    - Run Jupyter Notebook:
      ```sh
      jupyter notebook
      ```
    - Within Jupyter, you can create a new Python notebook and copy your code into the cells. Cells can be run independently and the outputs are displayed below each cell.

2. **Create API Endpoints for Game Mechanics**

    In order to increase the flexibility and scalability of the game, you could develop a RESTful API using a framework such as Flask or Django. This API could handle actions such as spinning the wheel, making a guess, or checking the scores, and could be accessed from various front-ends (web, mobile, etc.)

    To develop an API, you could do the following:

    - Set up a new Flask or Django project.
    - Create endpoints for each of the game actions, i.e., `/spin`, `/guess`, `/buy_vowel`, and `/solve`.
    - Modify the game logic to make HTTP requests to these endpoints instead of directly calling Python functions.
    - Deploy your API on a server.

3. **Integrate with a Front-end Interface**

    Instead of interacting with the game through a terminal or Jupyter notebook, a front-end interface could be developed to handle user inputs and display the game state. This could be a web-based interface developed using HTML/CSS/JavaScript, or a mobile app developed using a framework like React Native or Flutter.


5. **Include a Database for Persistent Data**

    A database could be incorporated to store game state, player scores, and game history. This would allow players to resume games, view past scores, and track their performance over time. SQL or NoSQL databases such as MySQL, PostgreSQL, or MongoDB could be used for this purpose.

