#!coding=utf8
import unittest

import random
from src.gale_shapely.gale_shapely import gale_shapely


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

    def test_simple_case(self):
        p = {0: [0, 1], 1: [0, 1], 2: [0, 1], 3: [1, 0]}
        t = {0: [3, 1, 0, 2], 1: [1, 2, 3, 0]}
        self.run_gs(p, t)

    def run_gs(self, p, t):
        matches = gale_shapely(t, p)
        for key in p:
            p[key] = {item: i for i, item in enumerate(p[key])}

        for key in t:
            t[key] = {item: i for i, item in enumerate(t[key])}

        self.assertNotEqual(len(matches), 0)
        for team, player in matches:
            for other_team in p[player].keys():
                if other_team == team:
                    continue
                # Comparo los matches (team, player) con (other_team, other_player)
                # Hay inestabilidad si team prefiere a other_player antes que a player,
                # y other_team prefiere a player antes que a other_player
                for _team, other_player in matches:
                    if _team != other_team:
                        continue

                    player_prefers_other_team = p[player][other_team] < p[player][team]
                    other_team_prefers_player = t[other_team][player] < t[other_team][other_player]

                    team_prefers_other_player = t[team][other_player] < t[team][player]
                    other_player_prefers_team = p[other_player][team] < p[other_player][other_team]

                    self.assertFalse((player_prefers_other_team and other_team_prefers_player) or
                                     (team_prefers_other_player and other_player_prefers_team))
