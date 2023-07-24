# Wheel of Reason for Language Models

Welcome to Wheel of Reason, an intriguing and challenging game specifically designed for large language models, often employed through a front-end interface such as ChatGPT, bard.google.com , Claude v2 etc. This game tests the model's reasoning skills and vocabulary comprehension.

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

## Notes

This game is currently interactive and requires manual user input for all player actions. The players' names are hardcoded and each player's actions are performed by user input in the console.

To run the game in a non-interactive environment, you would need to modify the source code to provide player actions programmatically or through some other interface.


