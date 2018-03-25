from numpy import random

NUM_OF_PLAYERS = 200
NUM_OF_TEAMS = 20
VACANCIES_PER_TEAM = 10

preferences = []

# create an array of random numbers from 0 to NUM_OF_PLAYERS for each team.
for i in range(NUM_OF_PLAYERS):
    preferences.append(random.choice(NUM_OF_TEAMS, size=NUM_OF_TEAMS, replace=False) + 1)


# save data to files
base_filename = "jugador_"

for i in range(NUM_OF_PLAYERS):
    current_filename = base_filename + str(i + 1) + ".prf"
    f = open(current_filename, 'w')
    for j in range(NUM_OF_TEAMS):
        f.write(str(preferences[i][j]) + '\n')
    f.close()
