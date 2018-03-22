from numpy import random 
NUM_OF_PLAYERS = 200
NUM_OF_TEAMS = 20
VACANCIES_PER_TEAM = 10

preferences = []

for i in range(0,NUM_OF_TEAMS):
    preferences.append(random.choice(NUM_OF_PLAYERS, size=NUM_OF_PLAYERS, replace=False))

for i in range(0, NUM_OF_TEAMS):
    print(i, preferences[i])
