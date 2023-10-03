TEAMS = [
    'Panthers',
    'Bandits',
    'Warriors',
]

PLAYERS = [{
        'name': 'Karl Saygan',
        'guardians': 'Heather Bledsoe',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Matt Gill',
        'guardians': 'Charles Gill and Sylvia Gill',
        'experience': 'NO',
        'height': '40 inches'
    },
    {   'name': 'Sammy Adams',
        'guardians': 'Jeff Adams and Gary Adams',
        'experience': 'NO',
        'height': '45 inches'
    },
    {
        'name': 'Chloe Alaska',
        'guardians': 'David Alaska and Jamie Alaska',
        'experience': 'NO',
        'height': '47 inches'
    },
    {
        'name': 'Bill Bon',
        'guardians': 'Sara Bon and Jenny Bon',
        'experience': 'YES',
        'height': '43 inches'
    },
    {
        'name': 'Joe Kavalier',
        'guardians': 'Sam Kavalier and Elaine Kavalier',
        'experience': 'NO',
        'height': '39 inches'
    },
    {
        'name': 'Phillip Helm',
        'guardians': 'Thomas Helm and Eva Jones',
        'experience': 'YES',
        'height': '44 inches'
    },
    {
        'name': 'Les Clay',
        'guardians': 'Wynonna Brown',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Sal Dali',
        'guardians': 'Gala Dali',
        'experience': 'NO',
        'height': '41 inches'
    },
    {
        'name': 'Suzane Greenberg',
        'guardians': 'Henrietta Dumas',
        'experience': 'YES',
        'height': '44 inches'
    },
    {
        'name': 'Jill Tanner',
        'guardians': 'Mark Tanner',
        'experience': 'YES',
        'height': '36 inches'
    },
    {
        'name': 'Arnold Willis',
        'guardians': 'Claire Willis',
        'experience': 'NO',
        'height': '43 inches'
    },
    {
        'name': 'Herschel Krustofski',
        'guardians': 'Hyman Krustofski and Rachel Krustofski',
        'experience': 'YES',
        'height': '45 inches'
    },
    {
        'name': 'Eva Gordon',
        'guardians': 'Wendy Martin and Mike Gordon',
        'experience': 'NO',
        'height': '45 inches'
    },
    {
        'name': 'Ben Finkelstein',
        'guardians': 'Aaron Lanning and Jill Finkelstein',
        'experience': 'NO',
        'height': '44 inches'
    },
    {
        'name': 'Joe Smith',
        'guardians': 'Jim Smith and Jan Smith',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Diego Soto',
        'guardians': 'Robin Soto and Sarika Soto',
        'experience': 'YES',
        'height': '41 inches'
    },
    {
        'name': 'Kimmy Stein',
        'guardians': 'Bill Stein and Hillary Stein',
        'experience': 'NO',
        'height': '41 inches'
    }
]

#The below are strings for the menu options
BALL = '''
            ..ee$$$$$ee..
        .e$*""    $    ""*$e.
      z$"*.       $         $$c
    z$"   *.      $       .P  ^$c
   d"      *      $      z"     "b
  $"        b     $     4%       ^$
 d%         *     $     P         '$
.$          'F    $    J"          $r
4L...........b....$....$...........J$
$F           F    $    $           4$
4F          4F    $    4r          4P
^$          $     $     b          $%
 3L        .F     $     'r        JP
  *c       $      $      3.      z$
   *b     J"      $       3r    dP
    ^$c  z%       $        "c z$"
      "*$L        $        .d$"
         "*$ee..  $  ..ze$P"
             ""*******""
'''
INTRO = "🏀 BASKETBALL TEAM STATS TOOL 🏀"
MENU = "---- MENU----\n"
CHOICES = "Here are your choices:"
ENTER_OPTION = "Enter an option:  "
ENTER_CONTINUE = "Press ENTER to continue..."
SPACER = "--------------------------------------------"
SPACER_BLANK = " "
GOODBYE_MESSAGE = "Thanks for using the Basketball Stats Tool. Goodbye!"

OPTION_ERROR = "Please enter a valid option."

#formattable constants for team stats
TEAM = "Team: {} Stats"
TOTAL_PLAYERS = "Total Players: {}"
TOTAL_EXPERIENCED = "Total Experienced: {}"
TOTAL_INEXPERIENCED = "Total Inexperienced: {}"
AVERAGE_HEIGHT = "Average Height: {}\n"
PLAYERS_ON_TEAM = "Players on Team:\n   {}\n"
GUARDIANS = "Guardians:\n   {}\n"