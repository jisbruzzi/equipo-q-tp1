#!coding=utf8
import unittest

from src.gale_shapely.gale_shapely import gale_shapely
import random


class GSTest(unittest.TestCase):

    def test_random_preferences(self):
        teams = 100
        players = 1000

        players_list = [i for i in range(players)]
        t = {}
        for i in range(teams):
            random.shuffle(players_list)
            t[i] = players_list.copy()

        teams = list(t.keys())
        p = {}
        for i in range(players):
            random.shuffle(teams)
            p[i] = teams.copy()

        self.run_gs(p, t)

    def test_same_team_prefs(self):
        teams = 100
        players = 1000

        t = {
            i: [j for j in range(players)]
            for i in range(teams)
        }

        teams = list(t.keys())
        p = {}
        for i in range(players):
            random.shuffle(teams)
            p[i] = teams.copy()

        self.run_gs(p, t)

    def test_same_player_prefs(self):
        teams = 100
        players = 1000

        players_list = [i for i in range(players)]
        t = {}
        for i in range(teams):
            random.shuffle(players_list)
            t[i] = players_list.copy()

        p = {
            i: [j for j in range(teams)]
            for i in range(players)
        }

        self.run_gs(p, t)

    def run_gs(self, p, t):
        vacants = int(len(p) / len(t))
        matches = gale_shapely(t, p, vacants)
        for team, player in matches:
            for other_team in p[player][:p[player].index(team)]:
                other_team_matches = filter(lambda x: x[0] == other_team, matches)
                # Comparo los matches (team, player) con (other_team, other_player)
                # Hay inestabilidad si team prefiere a other_player antes que a player,
                # y other_team prefiere a player antes que a other_player
                for _, other_player in other_team_matches:
                    check = \
                        t[other_team].index(player) < t[other_team].index(other_player) and \
                        t[team].index(player) > t[team].index(other_player)
                    self.assertFalse(check,
                                     "Inestabilidad: {} {}".format((team, player), (other_team, other_player)))
