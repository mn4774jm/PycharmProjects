""""
ICS Problem 2.2.8 Strategy Game: PS Rock

Execute this file psrock_play.py to play a tournament.
psrock.py implements the round robin tournament of rock paper scissors

Prior to execution:
Line 22: Type each team's module name (the file name, but without the py) on the import statement,
Lines 27-30: Create a reload() statement for each module, and
Original line 36: Place each module name as an arugment to the function psrock.round_robin().
Each player should have their own .py file containing
a function called move(my_history, their_history)
These filenames (without the .py extension) are passed to the
round_robin() function as the 2nd, 3rd, etc. arguments.

(c) 2015 Project Lead The Way, Inc.
"""

import psrock
from importlib import reload
reload(psrock)

import team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, team6m, team7m, team8m, team10m, team11m, team14m # add team name in 3 places!
# The reload() statement is needed for each team because import 
# will only compile source code once to create the pyc file and store in memory.
# Without reload(), changes to the .py file will be ignored unless the pyc 
# file is deleted and the kernel restarted. 
reload(team1) 
reload(team2)
reload(team3)
reload(team4)
reload(team5)
reload(team6) #turn on other team numbers, as needed (2nd of 3 places for team names)
reload(team7)
reload(team8)
reload(team9)
reload(team10)
reload(team6m) 
reload(team7m)
reload(team8m)
#reload(team9m) # DQ'd - copy of team 2
reload(team10m)
reload(team11m)
# reload(team12m) # turned off due to errors
reload(team14m)

                        
# The first argument of round_robin() specifies the number of 
# rounds to be played by each pair of strategies. 
# Change the other arguments to use more teams, fewer teams, or different teams
short_report, long_report = psrock.round_robin(20, team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, team6m, team7m, team8m, team10m, team11m, team14m)
# add other team names to line above, if needed. this is the 3rd of 3 places needing the team names

for team in long_report:
    print('-'*80)
    print(long_report[team])
    
print(short_report)