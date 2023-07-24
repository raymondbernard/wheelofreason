import pytest
from wor import Player, Game, load_wheel, load_phrases

# Load the wheel configuration from a JSON file
WHEEL = load_wheel('wheel.json')

# Load the categories and phrases from a JSON file
PHRASES = load_phrases('categories.json')

def test_player_initialization():
    player = Player("Alice")
    assert player.name == "Alice"
    assert player.score == 0
    assert len(player.guessed_letters) == 0

def test_game_initialization():
    players = [Player("Alice"), Player("Bob")]
    game = Game(players)
    assert len(game.players) == 2
    assert game.category in PHRASES.keys()
    assert game.phrase in PHRASES[game.category]
    assert len(game.guessed) == 0
    assert game.log_file.startswith("log_")
    assert game.log_file.endswith(".json")
