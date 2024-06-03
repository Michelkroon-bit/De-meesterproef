from Data import *
import random
teams = []
team = {}

print(zinnen[0])
team_1 = input(zinnen[1])
team_2 = input(zinnen[2])
team["team 1"] = team_1
team["team 2"] = team_2
teams.append(team)

te_raden = random.choice(words)
print(te_raden) # for debugging
print(te_raden[0] + "_" * (len(te_raden) - 1))

