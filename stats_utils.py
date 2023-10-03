import team_utils
import constants
from classes import MenuOptions
from classes import Team

#the function that starts the stats tool. If this is the first call, display
#the welcome message first.
def start_stats():

    #init the options and teams
    options = list(MenuOptions)
    teams = team_utils.balance_teams(team_utils.clean_data())

    #print the initial strings
    print(constants.MENU)
    print(constants.CHOICES)

    #print all options in a numbered list
    for i, option in enumerate(options, 1):
        print(f'{i}) {option.value}')
    
    #print a blank line
    print(constants.SPACER_BLANK)

    #get user input for option choice
    while True:
        try:
            #get the choice and check if it is a valid option
            choice = int(input(constants.ENTER_OPTION))
            if choice not in range(1, len(options) + 1):
                raise ValueError
            #if the choice is valid, get the option from the list of options
            if choice == 1:
                #if the option is quit, call quit()
                quit()
            elif choice == 2:
                #if the option is display stats, call choose_team()
                choose_team(teams)

            break
        except ValueError:
            #if the choice is not valid, print OPTION_ERROR and try again
            print(constants.OPTION_ERROR)

#display the welcome message
def display_welcome():
    print(constants.BALL)
    print(constants.INTRO)

#choose a team to display stats for
def choose_team(teams: list[Team]):

    #print an initial blank line
    print(constants.SPACER_BLANK)

    #print all teams in a numbered list
    for i, team in enumerate(teams, 1):
        print(f'{i}) {team.name}')

    #print a blank line
    print(constants.SPACER_BLANK)

    #get user input for team choice
    while True:
        try:
            #get the choice and check if it is a valid option
            choice = int(input(constants.ENTER_OPTION))
            if choice not in range(1, len(teams) + 1):
                raise ValueError
            #get the team from the list of teams
            team = teams[choice - 1]
            #display the stats for the team
            display_stats(team)

            break
        except ValueError:
            #if the choice is not valid, print OPTION_ERROR and try again
            print(constants.OPTION_ERROR)

#quit the program
def quit():
    print(constants.GOODBYE_MESSAGE)
    exit()

#display the stats for a team
def display_stats(team: Team):

    #print a blank line
    print(constants.SPACER_BLANK)
    #print the team name
    print(constants.TEAM.format(team.name))
    #print a blank line
    print(constants.SPACER)
    #print the total players
    print(constants.TOTAL_PLAYERS.format(len(team.players)))

    #total experienced players
    exp_players = [player for player in team.players if player.experience]
    print(constants.TOTAL_EXPERIENCED.format(len(exp_players)))

    #total inexperienced players
    inexp_players = [player for player in team.players if not player.experience]
    print(constants.TOTAL_INEXPERIENCED.format(len(inexp_players)))

    #average height
    print(constants.AVERAGE_HEIGHT.format(team.avaerage_height()))

    #create a string of player names seperated by a comma and a space
    players = ', '.join([player.name for player in team.players])
    print(constants.PLAYERS_ON_TEAM.format(players))

    #create a string of guardian names seperated by a comma and a space
    #guardians contains multiple names seperated by 'and' so we need to split on 'and'
    #then we need to join the guardian names back together with a comma and a space
    #also remove any duplicated using set()
    guardians = ', '.join(set([guardian.strip() for player in team.players for guardian in player.guardians.split('and')]))
    print(constants.GUARDIANS.format(guardians))

    #show ENTER_CONTINUE and wait for user to press enter. Wheb they do, call start_stats() again
    enter = input(constants.ENTER_CONTINUE)

    start_stats()

# Ensuring script doesn't execute when imported
if __name__ == "__main__":
    display_welcome()  # Call to display welcome message
    teams = team_utils.balance_teams(team_utils.clean_data())  # Preparing teams data
    start_stats(teams)