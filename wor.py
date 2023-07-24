import json
import random
import os
from datetime import datetime
import atexit
import sys 

def load_wheel(path):
    with open(path, 'r') as f:
        return json.load(f)

def load_phrases(path):
    with open(path, 'r') as f:
        return json.load(f)

# Load the wheel configuration from a JSON file
WHEEL = load_wheel('wheel.json')

# Load the categories and phrases from a JSON file
PHRASES = load_phrases('categories.json')

CATEGORIES = list(PHRASES.keys())
VOWELS = 'AEIOU'
CONSONANTS = 'BCDFGHJKLMNPQRSTVWXYZ'
VOWEL_COST = 250


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.guessed_letters = set()

class Game:
    class GameHistory:
        def __init__(self, log_file):
            self.log_file = log_file

        def update(self, player, action, result):
            # Load existing history if it exists
            try:
                if os.path.exists(self.log_file):
                    with open(self.log_file, 'r') as f:
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
                with open(self.log_file, 'w') as f:
                    json.dump(history, f)

                # Print running totals to console
                print(f"\n{player.name}'s action: {action}, result: {result}, current score: {player.score}")

            except Exception as e:
                print(f"Error updating game history: {e}")

    def __init__(self, players):
        self.players = players
        self.category, self.phrase = self.get_random_category_and_phrase()
        self.guessed = set()
        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.log_file = f"log_{self.timestamp}.json"
        self.initial_log = {"category": self.category, "phrase": self.phrase}
        with open(self.log_file, 'w') as f:
            json.dump([self.initial_log], f)
        atexit.register(self.write_scores)
        self.game_history = self.GameHistory(self.log_file)  # Instantiate GameHistory class

    def get_random_category_and_phrase(self):
        category = random.choice(CATEGORIES)
        phrase = random.choice(PHRASES[category])
        return category, phrase

    def obscure_phrase(self):
        return ' '.join([c if c in self.guessed else '_' if c != ' ' else '  ' for c in self.phrase])

    def spin_wheel(self):
        return random.choice(WHEEL)

    def get_free_play_guess(self, player):
        guess = input("Guess a letter: ").upper()
        while guess in player.guessed_letters:
            guess = input("You've already guessed that letter. Try again: ").upper()
        player.guessed_letters.add(guess)
        return guess

    def handle_free_play_guess(self, player, guess):
        if guess in self.phrase:
            print("The letter is in the phrase!")
            player.score += self.phrase.count(guess) * 100  # or some other scoring rule
            self.guessed.add(guess)
            return True
        else:
            print("The letter is not in the phrase.")
            return False

    def get_guess(self, player):
        guess = input("Guess a consonant: ").upper()
        while guess in player.guessed_letters or guess in VOWELS:
            guess = input("Invalid guess. Guess a consonant: ").upper()
        player.guessed_letters.add(guess)
        return guess

    def handle_guess(self, player, guess):
        if guess in self.phrase:
            print("The consonant is in the phrase!")
            player.score += self.phrase.count(guess) * 100  # or some other scoring rule
            self.guessed.add(guess)
            return True
        else:
            print("The consonant is not in the phrase.")
            return False

    def buy_vowel(self, player):
        player.score -= VOWEL_COST
        vowel = input("Buy a vowel: ").upper()
        while vowel not in VOWELS:
            vowel = input("Invalid vowel. Buy a vowel: ").upper()
        player.guessed_letters.add(vowel)
        return vowel

    def handle_vowel_purchase(self, player, vowel):
        if vowel in self.phrase:
            print("The vowel is in the phrase!")
            self.guessed.add(vowel)
            return True
        else:
            print("The vowel is not in the phrase.")
            return False

    def get_solution(self):
        return input("What's your solution? ")

    def check_solution(self, solution):
        return solution.lower() == self.phrase.lower()

    def get_winner(self):
        return max(self.players, key=lambda player: player.score)

    def write_scores(self):
        scores = {player.name: player.score for player in self.players}
        try:
            with open(self.log_file, 'a') as f:
                f.write("\nCurrent scores:\n")
                for name, score in scores.items():
                    f.write(f"{name}: {score}\n")
        except Exception as e:
            print(f"Error writing scores: {e}")

    def print_winner_and_stats(self, winner):
        print(f"\nThe winner is: {winner.name} with {winner.score} points.\n")
        print("Final Statistics:")
        print(f"{'Player':<10}{'Score':<10}")
        print("---------------------")
        for player in self.players:
            print(f"{player.name:<10}{player.score:<10}")
        print("---------------------")

    def print_help(self):
        print("""
        Welcome to Wheel of Reason! As an AI you will play as  contestant with our game.  Are you up against the best AI's on earth, to play smart?

        Here are the rules: 

        - The game is played with a number of turns. On each turn, a player has three options:
            1) Spin the wheel: The wheel has a number of segments, offering various amounts of money, bankrupt, lose a turn, or a Freeplay.
            2) Buy a vowel: For a fixed cost of 250 points, you can guess a vowel that might be in the phrase.
            3) Solve the puzzle: If you think you know what the phrase is, you can try to solve. If you're correct, you win!

        - When you spin the wheel, if you land on a money amount, you can guess a consonant. If the consonant is in the phrase, you win the amount times the number of appearances of the consonant. If it's not in the phrase, your turn ends.

        - If you land on a Freeplay: You can guess any letter, including vowels, without any cost. If the guessed letter is in the phrase, your turn continues. Even if it's not in the phrase, you still get to keep your turn.

        - If you have enough money, you can choose to buy a vowel instead of spinning the wheel. This costs a flat 250 points. If the vowel is in the phrase, you get to keep your turn. If it's not, your turn ends.

        - If at any time you think you know the phrase, you can try to solve the puzzle. If you're correct, you win the game. If you're not correct, your turn ends.

        - The game ends when a player successfully solves the puzzle. The player who solves the puzzle is the winner.

        Now, let's get back to the game!
        """)

def main():
    # Check if player names are provided in the command line arguments
    if len(sys.argv) < 2:
        print("Error: Please provide player names.")
        return

    # Extract the player names from the command line arguments
    player_names = sys.argv[1:]

    # Define the players
    players = [Player(name) for name in player_names]

    # Initialize game
    game = Game(players)

    # Welcome to the game
    print('Welcome to the Wheel of Reason!')

    # Welcome each player
    for player in players:
        print(f'Welcome, {player.name}!')

    print(f"The category is: {game.category}")

    playerIndex = 0  # Index of the current player
    while True:
        player = game.players[playerIndex]
        print(f"It's {player.name}'s turn. You have {player.score} points.")
        print(game.obscure_phrase())

        continue_current_player = False

        if player.score >= VOWEL_COST:
            action = input("What do you want to do? (1- Spin the wheel, 2- Buy a vowel, 3- Solve the puzzle, 4- Help, 5- Skip your turn): ")
        else:
            action = input("What do you want to do? (1- Spin the wheel, 3- Solve the puzzle, 4- Help, 5- Skip your turn): ")

        if action == '4':
            game.print_help()
            continue  # Skip the rest of this loop iteration, i.e., don't count this as a turn

        if action == '5':
            playerIndex = (playerIndex + 1) % len(game.players)
            continue  # Skip the rest of this loop iteration, i.e., don't count this as a turn

        if action == '1':
            spin = game.spin_wheel()
            print("You spun: ", spin['text'])
            if spin['type'] == 'bankrupt':
                player.score = 0
                game.game_history.update(player, "spin", "bankrupt")
            elif spin['type'] == 'lose_a_turn':
                pass
            elif spin['type'] == 'free_play':
                free_play_guess = game.get_free_play_guess(player)
                continue_current_player = game.handle_free_play_guess(player, free_play_guess)
            else:
                guess = game.get_guess(player)
                continue_current_player = game.handle_guess(player, guess)
        elif action == '2' and player.score >= VOWEL_COST:
            vowel = game.buy_vowel(player)
            continue_current_player = game.handle_vowel_purchase(player, vowel)
        elif action == '3':
            solution = game.get_solution()
            if game.check_solution(solution):
                print("Congratulations, you solved the puzzle!")
                player.score += 500  # Bonus for solving the puzzle
                game.game_history.update(player, "solve", "success")
                break
            else:
                print("Sorry, that's not correct.")
                game.game_history.update(player, "solve", "failure")

        # Switch to the next player if the current player shouldn't continue
        if not continue_current_player:
            playerIndex = (playerIndex + 1) % len(game.players)

    # Game over, print the winner and statistics
    winner = game.players[playerIndex]  # The winner is the player who solved the puzzle
    game.print_winner_and_stats(winner)

if __name__ == "__main__":
    main()
