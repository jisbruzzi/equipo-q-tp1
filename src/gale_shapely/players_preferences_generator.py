# NOTE: this script works with teams and players counting from 0. This should be corrected.

from src.gale_shapely.generator import generate

NUM_OF_PLAYERS = 200
NUM_OF_TEAMS = 20

if __name__ == '__main__':
    teams = [team for team in range(1, NUM_OF_TEAMS + 1)]
    generate(teams, NUM_OF_PLAYERS, 'jugador')
