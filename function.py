import Data
import random
from termcolor import colored
from tabulate import tabulate
import string
import time
import sys


def typemachine_print(prompt, speed):
    for x in prompt:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(speed)
    return prompt


def switch_teams():
    if Data.current_team == Data.teamA:
        Data.current_team = Data.teamB
    else:
        Data.current_team = Data.teamA


def get_random_word(woorden_lijst):
    return random.choice(woorden_lijst)


def display_grid(attempts, word_length):
    grid_size = word_length
    print("\n" + "=" * (grid_size * 4 + 1))
    for attempt in attempts:
        row = "| "
        for cell in attempt:
            row += cell + " | "
        print(row)
        print("-" * (grid_size * 4 + 1))
    print("=" * (grid_size * 4 + 1) + "\n")


def play_lingo(te_raden):
    print(f"Team {Data.current_team['name']} is aan de beurt! Veel succes!")
    Data.incorrect_streak = 0
    beurt = 0
    attempts = [[te_raden[0]] + ["_"] * (len(te_raden) - 1)]
    display_grid(attempts, len(te_raden))

    while beurt < 5:
        woord_invullen = input(Data.zinnen[3])
        result = check_for_conditions(woord_invullen, te_raden, attempts)
        if result == "goed geraden":
            return result, te_raden
        elif result == "invalid input" or result == "invalid length":
            continue
        else:
            Data.incorrect_streak += 1
            if Data.incorrect_streak >= 3:
                Data.current_team["incorrect_streak"] += 1
                print(Data.zinnen[15])
                if Data.current_team["incorrect_streak"] == 3:
                    print(f"team {Data.current_team['name']} {Data.zinnen[17]}")
                    break
                else:
                    switch_teams()
                return "incorrect_streak", te_raden
                
        beurt += 1
    
    
    
    print("\n" + colored("Helaas, je hebt het woord niet geraden.", 'red'))
    print(f"Het juiste woord was: {te_raden}")
    return Data.zinnen[6], te_raden


def check_for_conditions(woord_invullen, te_raden, attempts):
    if woord_invullen == te_raden:
        print("\n" + colored("Goed geraden!", 'green'))
        geraden_letters = [colored(letter, 'green') for letter in te_raden]
        attempts.append(geraden_letters)
        display_grid(attempts, len(te_raden))
        Data.current_team["correct_words"] += 1
        Data.current_team["kaart"] = generate_bingokaart("odd" if Data.current_team == Data.teamA else "even")
        return "goed geraden"
    
    if len(woord_invullen) != len(te_raden):
        print(Data.zinnen[13])
        return "invalid length"

    for letter in set(woord_invullen):
        if woord_invullen.count(letter) >= 3:
            print("\n" + colored(Data.zinnen[11], 'red'))
            return "invalid input"
    
    geraden_letters = []
    for i, letter in enumerate(woord_invullen):
        if letter not in string.ascii_lowercase or letter == "":
            print(Data.zinnen[5])
            geraden_letters = [te_raden[0]] + ["_"] * (len(te_raden) - 1)
            attempts.append(geraden_letters)
            display_grid(attempts, len(te_raden))
            return "invalid input"

        if letter == te_raden[i]:
            geraden_letters.append(colored(letter, 'green'))
        elif letter in te_raden:
            geraden_letters.append(colored(letter, 'yellow'))
        else:
            geraden_letters.append(letter)
    
    attempts.append(geraden_letters)
    display_grid(attempts, len(te_raden))
    return "continue"


def generate_bingokaart(odd_or_even):
    bingokaart = []
    indiviuele_getallen = []
    gegenereerde_getallen = set()
    getal = 0
    max_number = 30

    while getal < 16:
        if odd_or_even == "odd":
            random_getal = random.randint(0, max_number) * 2 + 1
        else:
            random_getal = random.randint(0, max_number) * 2

        if random_getal not in gegenereerde_getallen:
            getal += 1
            indiviuele_getallen.append(random_getal)
            gegenereerde_getallen.add(random_getal) 
            if getal % 4 == 0:
                bingokaart.append(indiviuele_getallen)
                indiviuele_getallen = []
    
    return bingokaart


def display_bingokaart(bingokaart):
    print(tabulate(bingokaart, tablefmt="grid"))


def grab_bal():
    getrokken_ballen = []
    for x in range(2):
        if Data.current_team["even_or_odd"] == "odd":
            random_bal = random.choice(Data.ballen_odd)
            getrokken_ballen.append(random_bal)
            Data.ballen_odd.remove(random_bal)
        elif Data.current_team["even_or_odd"] == "even":
            random_bal = random.choice(Data.ballen_even)
            getrokken_ballen.append(random_bal)
            Data.ballen_even.remove(random_bal)
            
    return getrokken_ballen


def check_getrokken_ballen(getrokken_ballen):
    numerieke_ballen = []
    
    for bal in getrokken_ballen:
        if isinstance(bal, int):
            numerieke_ballen.append(bal)
        elif bal == "ROOD":
            Data.current_team["red_ball"] += 1
        elif bal == "GROEN":
            Data.current_team["green_ball"] += 1
            
    return numerieke_ballen


def check_win_or_loss():
    if Data.current_team["red_ball"] >= 3:
        print(f"Team {Data.current_team['name']} heeft verloren vanwege 3 rode ballen!")
        print("einde spel")
        exit()
    elif Data.current_team["green_ball"] >= 3:
        print(f"Team {Data.current_team['name']} heeft gewonnen vanwege 3 groene ballen!")
        print("einde spel")
        exit()
    else:
        return "continue"


def bingo_turn(team_name, kaart):
   
    
    Data.getrokken_ballen = grab_bal()
    if not Data.getrokken_ballen:
        print("Er zijn geen ballen beschikbaar om te trekken!")
        return None
    
    if len(Data.getrokken_ballen) != 2:
        print("Er is iets misgegaan, het aantal getrokken ballen is niet gelijk aan 2!")
        return None

    check_getrokken_ballen(Data.getrokken_ballen)
    status = check_win_or_loss()
    if status in ["won", "lost"]:
        return status

    print(f"Team {Data.current_team['name']} heeft de volgende ballen getrokken: {Data.getrokken_ballen}")
    mark_numbers_on_card(kaart, Data.getrokken_ballen)
    display_bingokaart(kaart)  

    return "continue"


def mark_numbers_on_card(kaart, getrokken_ballen):
    for ball in getrokken_ballen:
        for i, row in enumerate(kaart):
            for j, number in enumerate(row):
                if number == ball:
                    kaart[i][j] = colored("X", 'yellow')


def check_for_bingo(kaart):
    print("Controleren op bingo in de kaart:")
    
    yellow_X = colored("X", 'yellow')

    # horizontale bingo
    for rij in kaart:
        if rij.count(yellow_X) == len(rij):
            return True

    # verticale bingo
    for kolom in range(len(kaart[0])):
        if sum(rij[kolom] == yellow_X for rij in kaart) == len(kaart):
            return True

    # diagonaal 
    if sum(kaart[i][i] == yellow_X for i in range(len(kaart))) == len(kaart):
        return True

    # andere diagonaal
    if sum(kaart[i][len(kaart) - 1 - i] == yellow_X for i in range(len(kaart))) == len(kaart):
        return True

    print("Er is nog geen bingo gevonden, het andere team is nu aan de beurt")
    return False
