import Data
import random
from function import *
from termcolor import colored

print(Data.zinnen[0])
team_1 = input(Data.zinnen[1])
team_2 = input(Data.zinnen[2])

Data.teamA = {
    "name": team_1,
    "red_ball": 0,
    "green_ball": 0,
    "correct_words": 0,
    "lingo": False,
    "even_or_odd": "odd",
    "kaart": generate_bingokaart("odd"),
    "incorrect streak" : 0
}

Data.teamB = {
    "name": team_2,
    "red_ball": 0,
    "green_ball": 0,
    "correct_words": 0,
    "lingo": False,
    "even_or_odd": "even",
    "kaart": generate_bingokaart("even"),
    "incorrect_streak" : 0
}

Data.current_team = Data.teamA

bingokaart_teamA = generate_bingokaart("odd")
bingokaart_teamB = generate_bingokaart("even")


while Data.current_team["lingo"] == False :
    random_word = get_random_word(Data.words)
    print(random_word)

    result, te_raden = play_lingo(random_word)

    if result == "goed geraden":
        typemachine_print(Data.zinnen[8], 0.10)

        if Data.current_team == Data.teamA:
            bingokaart = bingokaart_teamA
        else:
            bingokaart = bingokaart_teamB

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
        
        switch_teams()


#all(cell == yellow_dot for cell in rij) controleert of elke cel in de huidige rij gemarkeerd is met yellow_dot.