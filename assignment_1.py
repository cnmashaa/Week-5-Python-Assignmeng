class Tennis:
    def __init__(self, name, ranking, matches_won):
        self.name = name  # Player's name
        self.ranking = ranking  # Player's ranking
        self.matches_won = matches_won  # Matches won by player

    def serve(self):
        print(f"{self.name} serves the ball.")

    def hit(self):
        print(f"{self.name} hits the ball.")

    def show_stats(self):
        print(f"Player: {self.name}")
        print(f"Ranking: {self.ranking}")
        print(f"Matches Won: {self.matches_won}")

# Example of creating a Tennis object
player1 = Tennis("Roger Federer", 1, 103)
player1.serve()
player1.hit()
player1.show_stats()
