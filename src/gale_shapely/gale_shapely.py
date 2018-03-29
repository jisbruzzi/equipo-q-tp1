#!coding=utf8

# Implementacion del algoritmo. Empecemos por la version 1:1...

from .queue import Queue


def gale_shapely(team_prefs: dict, player_prefs: dict) -> set:
    """

    :param team_prefs: { team: [player1, player2, ...] , ... }
    :param player_prefs: { player: [team1, team2, ...], ... }
    :return:
    """

    vacants = int(len(player_prefs) / int(len(team_prefs)))
    teams = {team: {'prefs': team_prefs[team], 'current': 0, 'vacants': vacants} \
            for team in team_prefs}

    teams_queue = Queue(*[team for team in teams])

    player_prefs = player_prefs.copy()
    for key in player_prefs:
        player_prefs[key] = {item: i for i, item in enumerate(player_prefs[key])}

    final_set = {}
    while teams_queue:
        team = teams_queue.pop()
        prefs = teams[team]['prefs']
        current = teams[team]['current']
        while teams[team]['vacants']:
            player = prefs[current]
            other_team = final_set.get(player)
            if other_team is None:
                final_set[player] = team
                teams[team]['vacants'] -= 1

            elif player_prefs[player][team] < player_prefs[player][other_team]:
                final_set[player] = team
                teams[team]['vacants'] -= 1

                teams[other_team]['vacants'] += 1
                if teams[other_team]['vacants'] == 1:
                    teams_queue.enqueue(other_team)

            current += 1
        teams[team]['current'] = current

    return set([(team, player) for player, team in final_set.items()])

