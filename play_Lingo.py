from Data import *
import random
from function import * 
from termcolor import colored


# random_Words = get_random_word(words)
# play_game_lingo = play_lingo(random_Words)

# if play_game_lingo == "goed geraden":
#     typemachine_print(zinnen[8], 0.10)
#     bingokaart = generate_bingokaart()
#     display_bingokaart(bingokaart)

print(zinnen[0])
random_Words = get_random_word(words)
play_game_lingo = play_lingo(random_Words)
if play_game_lingo == "goed geraden":
    typemachine_print(zinnen[8], 0.10)
    bingokaart = generate_bingokaart()
    display_bingokaart(bingokaart)
    