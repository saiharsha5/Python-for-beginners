class Player:
    def __init__(self, player_name):
        self.player_name = player_name


class Tournament:
    def __init__(self):
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def final_score(self):
        return sum(self.scores)

    def generate_report(self, player):
        print("=" * 50)
        print("            TOURNAMENT REPORT")
        print("=" * 50)

        print(f"\nPlayer Name : {player.player_name}")
        print(f"\nFinal Score : {self.final_score()}")
        print("\nRank Status : QUALIFIED")

        print("\n" + "=" * 50)


player = Player("Raju")

tournament = Tournament()

tournament.add_score(100)
tournament.add_score(150)
tournament.add_score(200)

tournament.generate_report(player)