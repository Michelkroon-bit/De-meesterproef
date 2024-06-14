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
    "even_or_odd":"odd",
    "kaart": generate_bingokaart("odd")
}

Data.teamB = {
    "name": team_2, 
    "red_ball": 0, 
    "green_ball": 0, 
    "correct_words": 0, 
    "lingo": False, 
    "even_or_odd":"even",
    "kaart": generate_bingokaart("even")
}

Data.current_team = Data.teamA

bingokaart_teamA = generate_bingokaart("odd")
bingokaart_teamB = generate_bingokaart("even")

while True:
    random_word = get_random_word(Data.words)
    print(random_word)
    
    result, te_raden = play_lingo(random_word)


    if result == "goed geraden":
        typemachine_print(Data.zinnen[8], 0.10)
        odd_or_even = "odd" if Data.current_team == Data.teamA else "even"
        
        if Data.current_team == Data.teamA:
            bingokaart = bingokaart_teamA
        else:
            bingokaart = bingokaart_teamB
            
        bingo_turn(Data.current_team["name"], bingokaart)
        getrokken_ballen = grab_bal()
        
        mark_numbers_on_card(bingokaart, getrokken_ballen)  
        display_bingokaart(bingokaart)
        switch_teams()
        
    else:
        
        switch_teams()
        