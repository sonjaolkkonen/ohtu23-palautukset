from player_reader import PlayerReader
from enum import Enum

#def sort_by_points(player):
    #return player.points

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, player_reader):
        self._player_reader = player_reader

        self._players = player_reader.get_players()


    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by = SortBy.POINTS):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda player: (
                player.goals if sort_by == SortBy.GOALS else 0,
                player.assists if sort_by == SortBy.ASSISTS else 0,
                player.points if sort_by == SortBy.POINTS else 0
            )
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
