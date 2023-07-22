import json
import random
import os
from datetime import datetime
import atexit

# Load the wheel configuration from a JSON file
with open('wheel.json', 'r') as f:
    WHEEL = json.load(f)

# Load the categories and phrases from a JSON file
with open('phrases.json', 'r') as f:
    PHRASES = json.load(f)

CATEGORIES = list(PHRASES.keys())

VOWELS = 'AEIOU'
CONSONANTS = 'BCDFGHJKLMNPQRSTVWXYZ'
VOWEL_COST = 250

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

def spinWheel():
    return random.choice(WHEEL)

def getRandomCategoryAndPhrase():
    category = random.choice(CATEGORIES)
    phrase = random.choice(PHRASES[category])
    return category, phrase

def obscurePhrase(phrase, guessed):
    return ''.join('_ ' if letter not in guessed else letter for letter in phrase)

def getGuess():
    while True:
        guess = input("Enter your guess: ").upper()
        if len(guess) == 1 and guess in CONSONANTS:
            return guess
        else:
            print("Invalid guess. Please enter a consonant.")

def buyVowel(player):
    while True:
        vowel = input("Enter a vowel: ").upper()
        if len(vowel) == 1 and vowel in VOWELS:
            player.score -= VOWEL_COST
            return vowel
        else:
            print("Invalid input. Please enter a vowel.")

def updateGameHistory(player, action, result, log_file):
    # Load existing history if it exists
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            history = json.load(f)
    else:
        history = []

    # Add the new gameplay event
    event = {
        "player": player.name,
        "action": action,
        "result": result,
        "score": player.score
    }
    history.append(event)

    # Save the updated game history
    with open(log_file, 'w') as f:
        json.dump(history, f)

def getWinner(players):
    return max(players, key=lambda player: player.score)

def writeScores(players, log_file):
    scores = {player.name: player.score for player in players}
    with open(log_file, 'a') as f:
        f.write("\nCurrent scores:\n")
        for name, score in scores.items():
            f.write(f"{name}: {score}\n")

def main():
    players = [Player('ChatGPTv4 1'), Player('Google Bert(aka Bard) 2'), Player('LaMMA')]
    print('Welcome to Wheel of Fortune!')
    category, phrase = getRandomCategoryAndPhrase()
    guessed = set()
    print(f"The category is: {category}")

    # Generate a timestamp and create a unique log file for this game
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    log_file = f"log_{timestamp}.json"

    atexit.register(writeScores, players, log_file)

    playerIndex = 0
    while True:
        player = players[playerIndex]
        print(f"It's {player.name}'s turn. You have {player.score} points.")
        print(obscurePhrase(phrase, guessed))

        action = input("What do you want to do? (1- Spin the wheel, 2- Buy a vowel, 3- Solve the puzzle): ")
        if action == '1':
            spin = spinWheel()
            print("You spun: ", spin['text'])
            if spin['type'] == 'bankrupt':
                player.score = 0
                updateGameHistory(player, "spin", "bankrupt", log_file)
            elif spin['type'] == 'lose_a_turn':
                pass
            else:
                guess = getGuess()
                if guess in phrase:
                    player.score += spin['value']
                    guessed.add(guess)
                    updateGameHistory(player, "spin", f"guessed {guess}", log_file)
                else:
                    print("Sorry, that letter is not in the phrase.")
        elif action == '2':
            if player.score < VOWEL_COST:
                print(f"You don't have enough points to buy a vowel. You currently have {player.score} points.")
            else:
                vowel = buyVowel(player)
                if vowel in phrase:
                    guessed.add(vowel)
                    updateGameHistory(player, "bought vowel", f"guessed {vowel}", log_file)
                else:
                    print("Sorry, that letter is not in the phrase.")
        elif action == '3':
            guess = input("What's your solution? ").upper()
            if guess == phrase:
                print(f"Congratulations, {player.name}! You solved the puzzle!")
                updateGameHistory(player, "solved", "won", log_file)
                break
            else:
                print("Sorry, that's not correct.")

        playerIndex = (playerIndex + 1) % len(players)

if __name__ == '__main__':
    main()
