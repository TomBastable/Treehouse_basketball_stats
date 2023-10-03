from classes import Player, Team
from typing import Dict
from itertools import cycle
from collections import defaultdict
import copy
import constants

#clean the data
def clean_data():
    """
    Read the existing player data from the PLAYERS constants provided in constants.py
    Clean the player data using copy.deepcopy().
    Save the cleaned data to a new collection.
    Data to be cleaned:

    Height: This should be saved as an integer
    Experience: This should be saved as a boolean value (True or False)
    """
    #deepcopy the PLAYERS constant
    players_copy = copy.deepcopy(constants.PLAYERS)

    #loop through the players and clean the data
    #I've used class based values for readability / no magic values
    for player in players_copy:

        player[Player.Keys.EXPERIENCE] = player_has_experience(player)

        player[Player.Keys.HEIGHT] = int(player[Player.Keys.HEIGHT].split()[0])

    players_cleaned = [Player(**player) for player in players_copy]

    return players_cleaned

#bool to check if player has experience - helps with readability
def player_has_experience(player):
    """
    Returns True if the player has experience, False otherwise.
    """
    return player[Player.Keys.EXPERIENCE] == Player.Keys.HAS_EXPERIENCE

#balance the teams
def balance_teams(players):

    #create a list of teams
    teams = [Team(name, []) for name in copy.deepcopy(constants.TEAMS)]
    #create a list of experienced and inexperienced players
    exp_players, inexp_players = [], []

    #max players per team
    max_players = len(players) // len(teams)

    #loop through the players and add them to the appropriate list
    for player in players:
        (exp_players if player.experience else inexp_players).append(player)

    #loop throgh the teams and add half of max_player from each exp_players and inexp_players
    for team in teams:
        #add half of max_players from each list
        team.players += exp_players[:max_players // 2] + inexp_players[:max_players // 2]
        #remove the players we just added from the lists
        del exp_players[:max_players // 2]
        del inexp_players[:max_players // 2]

    return teams

# This block ensures the script only executes when run directly
if __name__ == "__main__":
    # Call your functions or logic here
    cleaned_data = clean_data()
    balanced_teams = balance_teams(cleaned_data)