# We will put all our functions here
# Noah Wahlquist, Andrew Wadley, Lex Bowman, and Crew Smith

'''
This is a file which uses functions to run a soccer game program. It will consist of functions for 
collecting team names, randomly assigning scores, and displaying outputs. Objects will be used for storing team info'''

import random as r

# Create lists for teams that the Home Team wins and loses against
lstWon = []
lstLost = []

# Create an empty list to add all of the away team objects to
lstTeams = []

# Create a class for the home team 
oHomeTeam = None
class Home_Team: 
    def __init__(self, team_name) : 
        self.team_name = team_name
        self.scores = []
        self.wins = None
        self.losses = None

# Create a class that will store necessary information for each away team
class Away_Team: 
    def __init__(self, team_name) : 
        self.team_name = team_name
        lstTeams.append(self)
        self.score = None


def Get_Team_Names() : 
    global oHomeTeam
    # Clear the lists in case they try to enter the team names again 
    lstTeams.clear()
    lstWon.clear()
    lstLost.clear()

    # Get the names of the home and away teams
    sHomeTeamName = input("Enter the name of the home team: ").title()
    oHomeTeam = Home_Team(sHomeTeamName)
    bContinue = True
    while bContinue == True : 
        try : 
            iNumTeams = int((input("Enter the number of teams played against: ")).strip())
            bContinue = False
        except : 
            print("Please enter a valid number of teams.")
    for team in range (1, iNumTeams + 1, 1) : 
        sAwayTeamName = input(f"Enter the name of team {team}: ").title()
        Away_Team(sAwayTeamName)
    print()


def Calculate_Scores() : 
    if len(lstTeams) == 0 : 
        print("Please enter the team names before trying to calculate scores")
    else : 
        # Clear the lists in case they run option 2 twice without choosing to start a new season
        # as this will run it with the same teams as before but won't make a second set of scores in each list
        lstWon.clear()
        lstLost.clear()
        if oHomeTeam is not None : 
            oHomeTeam.scores.clear()
        
        # Create placeholder variables for the running total number of wins and losses
        iWinCount = 0
        iLossCount = 0

        # Create loop for all games
        for team in lstTeams :
            iHomeTeamScore = r.randrange(0, 4)
            team.score = r.randrange(0, 4)
            #ensure there is no tie
            while iHomeTeamScore == team.score :
                iHomeTeamScore = r.randrange(0, 4)
                team.score = r.randrange(0, 4)
            # Update the win/loss total, add names to the right list
            if iHomeTeamScore > team.score : 
                lstWon.append(team)
                iWinCount = iWinCount + 1
            else : 
                lstLost.append(team)
                iLossCount = iLossCount + 1
            oHomeTeam.scores.append(iHomeTeamScore)

        # Add the win count and loss count as the win and loss attributes of the Home Team object
        oHomeTeam.wins = iWinCount
        oHomeTeam.losses = iLossCount

        print(f"Season record:")
        print(f"Wins: {iWinCount} | Losses: {iLossCount}")
        print()

def Search_Match():
    # Check if scores have actually been calculated first
    if not lstTeams or oHomeTeam.wins is None:
        print("Please enter teams and calculate scores (Options 1 & 2) before searching.")
        return

    sSearchName = input("Enter the name of the team you are looking for: ").title()
    bFound = False

    # Loop through the away teams to find a name match
    for iCount in range(len(lstTeams)):
        if lstTeams[iCount].team_name == sSearchName:
            print(f"\nMatch Found:")
            print(f"{oHomeTeam.team_name}: {oHomeTeam.scores[iCount]}")
            print(f"{lstTeams[iCount].team_name}: {lstTeams[iCount].score}")
            bFound = True
            break # Exit loop once found
    
    if not bFound:
        print(f"Team '{sSearchName}' was not found in this season's schedule.")
    print()

def Display_Menu() : 
    print("--- Soccer Game Menu --- ")
    print("1 - Enter the team names")
    print("2 - Determine the season record")
    print("3 - Search for a specific match score")
    print("4 - Display the full season's match details")
    print("5 - Start a new season")
    print("6 - Quit program")
    print()

    bContinue = True 
    while bContinue == True : 
        try : 
            iChoice = int(input("Enter your choice: "))
            if iChoice in range(1, 7) : 
                bContinue = False
            else : 
                print("Your choice must be between 1 and 6. Please try again.")
        except : 
            print("You must enter a number. Please try again.")
    print()
    return iChoice

def Run_Program() : 
    bContinueAll = True
    while bContinueAll == True : 
        
        # Display the menu
        iChoice = Display_Menu()
        
        # Collect the team names
        if iChoice == 1 : 
            Get_Team_Names()

        # Calculate the team scores
        elif iChoice == 2 : 
            Calculate_Scores()

        # Search for a specific match
        elif iChoice == 3:
            Search_Match()

        # Clear all of the lists to set up for a new season
        elif iChoice == 5 : 
            lstTeams.clear()
            lstWon.clear()
            lstLost.clear()
            if oHomeTeam is not None : 
                oHomeTeam.scores.clear()

        # Set condition to false to exit the program and give a thank-you message
        elif iChoice == 6 : 
            print("Thanks for using this soccer game program!")
            bContinueAll = False

# Run the program
Run_Program()