# NOTE: this script works with teams and players counting from 0. This should be corrected.
from numpy import random 

NUM_OF_PLAYERS = 200
NUM_OF_TEAMS = 20
VACANCIES_PER_TEAM = 10

preferences = []

# create an array of random numbers from 0 to NUM_OF_PLAYERS for each team.
for i in range(NUM_OF_TEAMS):
    preferences.append(random.choice(NUM_OF_PLAYERS, size=NUM_OF_PLAYERS, replace=False) + 1)


# save data to files
base_filename = "equipo_"

for i in range(NUM_OF_TEAMS):
    current_filename = base_filename + str(i+1) + ".prf"
    f = open(current_filename, 'w')
    for j in range(NUM_OF_PLAYERS):
        f.write(str(preferences[i][j]) + '\n')
    f.close()
