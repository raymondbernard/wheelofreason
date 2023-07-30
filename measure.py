class AIPerformance:
    def __init__(self, games_played, games_won, correct_guesses, total_guesses, total_turns, total_score, desirable_actions, undesirable_actions, incorrect_guesses, vowel_won, vowel_total):
        self.games_played = games_played
        self.games_won = games_won
        self.correct_guesses = correct_guesses
        self.total_guesses = total_guesses
        self.total_turns = total_turns
        self.total_score = total_score
        self.desirable_actions = desirable_actions
        self.undesirable_actions = undesirable_actions
        self.incorrect_guesses = incorrect_guesses
        self.vowel_won = vowel_won
        self.vowel_total = vowel_total

    def win_ratio(self):
        return (self.games_won / self.games_played) * 100

    def guess_accuracy(self):
        return (self.correct_guesses / self.total_guesses) * 100

    def efficiency(self):
        return self.total_turns / self.games_won

    def vowel_buying_strategy(self):
        with_vowel = (self.vowel_won / self.vowel_total) * 100
        without_vowel = ((self.games_won - self.vowel_won) / (self.games_played - self.vowel_total)) * 100
        return with_vowel - without_vowel

    def average_score(self):
        return self.total_score / self.games_played

    def information_use_score(self):
        return self.desirable_actions - self.undesirable_actions

    def standardized_information_use_score(self):
        return (self.desirable_actions - self.undesirable_actions) / self.total_turns

    def error_rate(self):
        return (self.incorrect_guesses / self.total_guesses) * 100

def main():
    # These are placeholder values
    ai = AIPerformance(100, 60, 400, 500, 200, 5000, 50, 10, 100, 30, 50)
    
    print(f"Win Ratio: {ai.win_ratio()}%")
    print(f"Guess Accuracy: {ai.guess_accuracy()}%")
    print(f"Efficiency: {ai.efficiency()}")
    print(f"Effectiveness of Vowel Buying Strategy: {ai.vowel_buying_strategy()}%")
    print(f"Average Score: {ai.average_score()}")
    print(f"Information Use Score: {ai.information_use_score()}")
    print(f"Standardized Information Use Score: {ai.standardized_information_use_score()}")
    print(f"Error Rate: {ai.error_rate()}%")

if __name__ == "__main__":
    main()
