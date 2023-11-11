from player import Player

class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader

    def top_scorers_by_nationality(self, nationality):
        players = self.player_reader.get_players()

        filtered_players = filter(lambda x: x.nationality == nationality, players)

        sorted_players = sorted(filtered_players, key=lambda x: x.points, reverse=True)

        return sorted_players
        
