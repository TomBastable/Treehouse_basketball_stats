from enum import Enum

# create a player class
class Player:
    
    #I'm not too sure about this class within a class...
    #It works for readability, but...I'm not sure how much
    #of a no-no it is, or even if I 100% like it...
    class Keys:
        HAS_EXPERIENCE = 'YES'
        NAME = 'name'
        GUARDIANS = 'guardians'
        EXPERIENCE = 'experience'
        HEIGHT = 'height'

    def __init__(self, name, guardians, experience, height):
        self.name = name
        self.guardians = guardians
        self.experience = experience
        self.height = height

#create an enum for menu options
class MenuOptions(Enum):
    QUIT = 'Quit'
    DISPLAY_STATS = 'Display Team Stats'

#create a team class
class Team:

    #average height function that gets the average height of players
    def avaerage_height(self):
        return int(sum([player.height for player in self.players]) / len(self.players))

    def __init__(self, name, players):
        self.name = name
        self.players = players