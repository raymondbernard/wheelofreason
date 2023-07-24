import json
import pytest
from wheelofreason import Player, spinWheel, getRandomCategoryAndPhrase, obscurePhrase  # assuming your game code is in game_file.py

# Mock data for tests
WHEEL = [
    {"type": "money", "text": "$600", "value": 600, "color": "blue", "name": "600"},
    {"type": "bankrupt", "text": "Bankrupt", "value": 0, "color": "black", "name": "Bankrupt"},
    {"type": "money", "text": "$650", "value": 650, "color": "blue", "name": "650"},
    {"type": "lose_a_turn", "text": "Lose a Turn", "value": 0, "color": "black", "name": "Lose a Turn"}
]
PHRASES = {
    "Phrase 1": ["HELLO", "WORLD"],
    "Phrase 2": ["TESTING", "123"]
}

# Test Player class
def test_Player():
    player = Player("Test")
    assert player.name == "Test"
    assert player.score == 0
    assert player.guessed_letters == set()

# Test spinWheel function
def test_spinWheel():
    spin = spinWheel()
    assert spin in WHEEL

# Test getRandomCategoryAndPhrase function
def test_getRandomCategoryAndPhrase():
    category, phrase = getRandomCategoryAndPhrase()
    assert category in PHRASES.keys()
    assert phrase in PHRASES[category]

# Test obscurePhrase function
def test_obscurePhrase():
    assert obscurePhrase("HELLO", set()) == "_____"
    assert obscurePhrase("HELLO", {"H"}) == "H____"
    assert obscurePhrase("HELLO", {"H", "E", "L", "O"}) == "HELLO"
