import random

# Define the wheel and other game components
WHEEL = [{'type': 'cash', 'value': 500, 'text': '$500'},
         {'type': 'cash', 'value': 1000, 'text': '$1000'},
         {'type': 'bankrupt', 'value': 0, 'text': 'Bankrupt'},
         {'type': 'lose_a_turn', 'value': 0, 'text': 'Lose a Turn'}]

CATEGORIES = ['Phrase', 'Person', 'Place', 'Thing', 'Title']
PHRASES = {'Phrase': ['A CHIP OFF THE OLD BLOCK', 'A FISH OUT OF WATER', 'A LEOPARD CANNOT CHANGE ITS SPOTS'],
           'Person': ['JOHN DOE', 'JANE DOE'],
           'Place': ['NEW YORK', 'PARIS'],
           'Thing': ['WHEEL OF FORTUNE', 'DICTIONARY'],
           'Title': ['THE GREAT GATSBY', 'BRAVE NEW WORLD']}
VOWELS = 'AEIOU'
CONSONANTS = 'BCDFGHJKLMNPQRSTVWXYZ'
VOWEL_COST = 250

# The player class
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

# Functions for the game logic
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

# The main game loop
def main():
    # Create the players
    players = [Player('ChatGPTv4 1'), Player('Google Bert(aka Bard) 2'), Player('LaMMA')]

    # Start the game
    print('Welcome to Wheel of Fortune!')
    category, phrase = getRandomCategoryAndPhrase()
    guessed = set()

    # Game rounds
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
            elif spin['type'] == 'lose_a_turn':
                pass
            else:
                guess = getGuess()
                if guess in phrase:
                    player.score += spin['value']
                    guessed.add(guess)
                    print(f"Good guess! Your score is now {player.score}")
                else:
                    print("Sorry, that letter is not in the phrase.")
        elif action == '2':
            if player.score < VOWEL_COST:
                print(f"You don't have enough points to buy a vowel. You currently have {player.score} points.")
            else:
                vowel = buyVowel(player)
                if vowel in phrase:
                    guessed.add(vowel)
                    print("Good guess!")
                else:
                    print("Sorry, that letter is not in the phrase.")
        elif action == '3':
            guess = input("What's your solution? ").upper()
            if guess == phrase:
                print(f"Congratulations, {player.name}! You solved the puzzle!")
                break
            else:
                print("Sorry, that's not correct.")

        playerIndex = (playerIndex + 1) % len(players)

if __name__ == '__main__':
    main()
