from player_reader import PlayerReader
from player import Player

from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerStats():
    def __init__(self, reader):
        self.reader = reader
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nat):
        '''
        top = []
        for player in self._players:
            if (player.nationality == nat):
                top.append(player)
        '''
        players_by_nationality = filter(
            lambda player: player.nationality == nat,
            self._players
        )

        p_list =list(players_by_nationality)

        def sort_by_points(player):
            return player.points

        sorted_players = sorted(
            p_list,
            reverse=True,
            key=sort_by_points
        )
        return sorted_players
    
    
    