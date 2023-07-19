import random

# The Wheel of Fortune wheel
WHEEL = [{'type': 'cash', 'value': 5000, 'text': '$5000'},
         {'type': 'bankrupt', 'value': 0, 'text': 'Bankrupt'},
         {'type': 'cash', 'value': 600, 'text': '$600'},
         {'type': 'lose_a_turn', 'value': 0, 'text': 'Lose a turn'},
         {'type': 'cash', 'value': 700, 'text': '$700'},
         {'type': 'cash', 'value': 900, 'text': '$900'},
         {'type': 'cash', 'value': 300, 'text': '$300'},
         {'type': 'cash', 'value': 800, 'text': '$800'},
         {'type': 'cash', 'value': 550, 'text': '$550'},
         {'type': 'cash', 'value': 400, 'text': '$400'},
         {'type': 'cash', 'value': 500, 'text': '$500'},
         {'type': 'cash', 'value': 450, 'text': '$450'}]

# The categories of phrases
CATEGORIES = ['Around The House', 'Food & Drink', 'Things', 'Living Things', 'Place']

# The phrases to guess
PHRASES = {'Around The House': ['ironing board', 'washing machine', 'dining table'],
           'Food & Drink': ['banana smoothie', 'roasted turkey', 'creamy pasta'],
           'Things': ['mirror', 'chair', 'pencil', 'notebook'],
           'Living Things': ['elephant', 'puppy', 'sparrow', 'human'],
           'Place': ['New York', 'India', 'Buckingham Palace', 'Mount Everest']}

# Players
PLAYERS = ['Human player #1', 'Human player #2', 'Human player #3']

def spinWheel():
    """Return a random item from the wheel."""
    return random.choice(WHEEL)

def getRandomCategoryAndPhrase():
    """Get a random category and phrase from PHRASES."""
    category = random.choice(CATEGORIES)
    phrase = random.choice(PHRASES[category])
    return category, phrase.lower()

def obscurePhrase(phrase, guessed):
    """Obscure each letter in the phrase that has not been guessed."""
    return ''.join('_ ' if letter != ' ' and letter not in guessed else letter for letter in phrase)

def showBoard(category, obscuredPhrase, guessed):
    """Show the category, obscured phrase, and letters guessed."""
    print('Category: ', category)
    print('Phrase: ', obscuredPhrase)
    print('Guessed: ', ', '.join(sorted(guessed)))

def getPlayerMove(player, category, obscuredPhrase, guessed):
    """Get a player's move."""
    print(player, "it's your turn!")
    while True:
        print("What do you want to do?")
        print("  1) Spin the wheel")
        print("  2) Buy a vowel for $250")
        print("  3) Solve the puzzle")
        option = input("> ")
        if option == '1':
            return spinWheel()
        elif option == '2':
            return 'buy_vowel'
        elif option == '3':
            return 'solve_puzzle'
        else:
            print("Invalid option. Try again.")

# Game loop
def main():
    print('Welcome to Wheel of Fortune!')
    
    category, phrase = getRandomCategoryAndPhrase()
    guessed = set()
    playerIndex = 0
    roundOver = False

    while not roundOver:
        player = PLAYERS[playerIndex]
        showBoard(category, obscurePhrase(phrase, guessed), guessed)
        
        move = getPlayerMove(player, category, obscurePhrase(phrase, guessed), guessed)
        
        if type(move) == dict:  # the player chose to spin the wheel
            if move['type'] == 'cash':
                print(player, "spins...")
                print(move['text'] + '!')
                guess = input("Guess a consonant: ").lower()
                if guess in guessed:
                    print("You've already guessed that letter.")
                elif guess in phrase:
                    print("Good guess!")
                    guessed.add(guess)
                else:
                    print("Sorry, that letter is not in the phrase.")
            elif move['type'] == 'bankrupt':
                print(player, "spins...")
                print(move['text'] + '!')
                print("You've gone bankrupt. You lose your turn.")
            elif move['type'] == 'lose_a_turn':
                print(player, "spins...")
                print(move['text'] + '!')
                print("You lose your turn.")

        elif move == 'buy_vowel':
            print(player, "chooses to buy a vowel.")
            guess = input("Guess a vowel: ").lower()
            if guess in guessed:
                print("You've already guessed that letter.")
            elif guess in phrase:
                print("Good guess!")
                guessed.add(guess)
            else:
                print("Sorry, that letter is not in the phrase.")

        elif move == 'solve_puzzle':
            print(player, "chooses to solve the puzzle.")
            guess = input("Guess the whole phrase: ").lower()
            if guess == phrase:
                print("Congratulations! You've solved the puzzle!")
                roundOver = True
            else:
                print("Sorry, that's not the correct phrase.")

        playerIndex = (playerIndex + 1) % len(PLAYERS)  # move on to the next player

if __name__ == '__main__':
    main()
