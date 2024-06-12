import Data 
import random
from function import * 
from termcolor import colored


# random_Words = get_random_word(words)
# play_game_lingo = play_lingo(random_Words)

# if play_game_lingo == "goed geraden":
#     typemachine_print(zinnen[8], 0.10)
#     bingokaart = generate_bingokaart()
#     display_bingokaart(bingokaart)

print(Data.zinnen[0])
team_1 = input(Data.zinnen[1])
team_2 = input(Data.zinnen[2])



Data.teamA = {"name": team_1, "red_ball": 0, "green_ball": 0, "correct_words": 0, "lingo": False, "kaart": generate_bingokaart("odd")}
Data.teamB = {"name": team_2, "red_ball": 0, "green_ball": 0, "correct_words": 0, "lingo": False, "kaart": generate_bingokaart("even")}

Data.current_team = Data.teamA

    
random_Words = get_random_word(words)
play_game_lingo = play_lingo(random_Words)
if play_game_lingo == "goed geraden":
    typemachine_print(zinnen[8], 0.10)
    bingokaart = generate_bingokaart()
    display_bingokaart(bingokaart)
    