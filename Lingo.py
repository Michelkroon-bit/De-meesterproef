from Data import *
import random

print(zinnen[0])
team_1 = input(zinnen[1])
team_2 = input(zinnen[2])
team["team 1"] = team_1
team["team 2"] = team_2
teams.append(team)

while rondes <3:
    te_raden = random.choice(words)
    print(te_raden) # for debugging
    print(te_raden[0] + "_" * (len(te_raden) - 1))

    while beurt <= 5:
        woord_invullen = input(zinnen[3])

        if woord_invullen == te_raden:
            print(zinnen [4])
            rondes +=1
            break
        else:
            print(zinnen [5])
            beurt += 1