from Data import *
import random
from function import * 
from termcolor import colored
 

print(zinnen[0])
team_1 = input(zinnen[1])
team_2 = input(zinnen[2])
team["team 1"] = team_1
team["team 2"] = team_2
teams.append(team)
te_raden = random.choice(words)

abc = play_lingo(te_raden)

if abc == "goed geraden":
    typemachine_print(f"{colored(te_raden,'green')}\n")
    typemachine_print(zinnen[8])
    #play_bingo()

