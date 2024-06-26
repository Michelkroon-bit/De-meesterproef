import Data
import random
from function import *
from termcolor import colored

# Predefine team names or generate them randomly
team_1 = "Team A"
team_2 = "Team B"

# Initialize teams
Data.teamA = {
    "name": team_1,
    "red_ball": 0,
    "green_ball": 0,
    "correct_words": 0,
    "lingo": False,
    "even_or_odd": "odd",
    "kaart": generate_bingokaart("odd")
}

Data.teamB = {
    "name": team_2,
    "red_ball": 0,
    "green_ball": 0,
    "correct_words": 0,
    "lingo": False,
    "even_or_odd": "even",
    "kaart": generate_bingokaart("even")
}

Data.current_team = Data.teamA

# Generate bingo cards
bingokaart_teamA = Data.teamA["kaart"]
bingokaart_teamB = Data.teamB["kaart"]

# Game loop for the bingo part
abx = 0
while Data.current_team["lingo"] == False :
    if Data.current_team == Data.teamA:
        bingokaart = bingokaart_teamA
    else:
        bingokaart = bingokaart_teamB

    # Simulate bingo turn
    getrokken_ballen = bingo_turn(Data.current_team["name"], bingokaart)
    if getrokken_ballen is None:
        continue

    numerieke_ballen = check_getrokken_ballen(getrokken_ballen)
    
    mark_numbers_on_card(bingokaart, getrokken_ballen)
    display_bingokaart(bingokaart)

    print(f"\n+----+-Team: {Data.current_team['name']}-+----+")
    print("+----+----+----+----+")
    print(f"|groene ballen:    {Data.current_team['green_ball']}|")
    print("+----+----+----+----+")
    print(f"|rode ballen:      {Data.current_team['red_ball']}|")
    print("+----+----+----+----+")
    print(f"|correcte woorden: {Data.current_team['correct_words']}|")
    print("+----+----+----+----+\n")

    abc = check_for_bingo(Data.current_team["kaart"])
    if abc:
        Data.current_team["lingo"] = True
        print(Data.zinnen[14])
        break
    else:
        switch_teams()
    abx +=1