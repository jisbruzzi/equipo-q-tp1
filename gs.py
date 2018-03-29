#!coding=utf8
"""
Módulo de entrada al algoritmo de Gale-Shapely. Carga los archivos de preferencias
en prefs/, los parsea y corre el algoritmo. Imprime los matches resultantes por salida estándar.
"""


import os

from src.gale_shapely.gale_shapely import gale_shapely

TEAMS = 20
PLAYERS = 200

PREFS_DIR = os.path.join(os.getcwd(), 'prefs')


def gs():
    players_prefs = {}
    for i in range(1, PLAYERS + 1):
        path = os.path.join(PREFS_DIR, 'jugador_{}.prf'.format(str(i)))
        with open(path) as f:
            players_prefs[i] = [int(line) for line in f.readlines()]

    teams_prefs = {}
    for i in range(1, TEAMS + 1):
        path = os.path.join(PREFS_DIR, 'equipo_{}.prf'.format(str(i)))
        with open(path) as f:
            teams_prefs[i] = [int(line) for line in f.readlines()]

    matches = gale_shapely(teams_prefs, players_prefs)
    for match in matches:
        print(match)


if __name__ == '__main__':
    gs()
