import Data 
import random
import string
import sys
import time
from termcolor import colored
from tabulate import tabulate

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

def get_team_data(team):
    print(team)

def get_random_word(woorden_lijst):
    return random.choice(Data.words)

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
    print(te_raden)
    
    beurt = 0
    attempts = [[te_raden[0]] + ["_"] * (len(te_raden) - 1)]
    display_grid(attempts, len(te_raden))

    while beurt < 5:
        woord_invullen = input(Data.zinnen[3])
        result = check_for_conditions(woord_invullen, te_raden, attempts)
        if result == "goed geraden":
            return "goed geraden", te_raden
        beurt += 1

    print("\n" + colored("Helaas, je hebt het woord niet geraden.", 'red'))
    print(f"Het juiste woord was: {te_raden}")
    return "niet geraden", te_raden

def check_for_conditions(woord_invullen, te_raden, attempts):
    if woord_invullen == te_raden:
        print("\n" + colored("Goed geraden!", 'green'))
        geraden_letters = [colored(letter, 'green') for letter in te_raden]
        attempts.append(geraden_letters)
        display_grid(attempts, len(te_raden))
        Data.current_team["correct_words"] += 1
        return "goed geraden"
    
    if len(woord_invullen) != len(te_raden):
        print(Data.zinnen[13])
        return "invalid length"

    geraden_letters = []
    for i, letter in enumerate(woord_invullen):
        if letter not in string.ascii_lowercase or letter == "":
            print("FOUTE INPUT!! alleen letters zijn toegestaan")
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
    getal = 0
    max_number = 30

    while getal < 16:
        if odd_or_even == "odd":
            random_getal = random.randint(0, max_number) * 2 + 1
        else:
            random_getal = random.randint(0, max_number) * 2

        if random_getal not in indiviuele_getallen:
            getal += 1
            indiviuele_getallen.append(random_getal)
            if getal % 4 == 0:
                bingokaart.append(indiviuele_getallen)
                indiviuele_getallen = []

    return bingokaart

def display_bingokaart(bingokaart):
    print(tabulate(bingokaart, tablefmt="grid"))

def mark_numbers_on_card(kaart, getrokken_ballen):
    for nummer in getrokken_ballen:
        for rij in kaart:
            for i in range(len(rij)):
                if rij[i] == nummer:
                    rij[i] = colored("X", 'red')
    return kaart

print(Data.zinnen[0])
team_1 = input(Data.zinnen[1])
team_2 = input(Data.zinnen[2])

Data.teamA = {
    "name": team_1, 
    "red_ball": 0, 
    "green_ball": 0, 
    "correct_words": 0, 
    "lingo": False, 
    "kaart": generate_bingokaart("odd")
}

Data.teamB = {
    "name": team_2, 
    "red_ball": 0, 
    "green_ball": 0, 
    "correct_words": 0, 
    "lingo": False, 
    "kaart": generate_bingokaart("even")
}

Data.current_team = Data.teamA

while True:
    random_word = get_random_word(Data.words)
    result, te_raden = play_lingo(random_word)

    if result == "goed geraden":
        typemachine_print(Data.zinnen[8], 0.10)
        odd_or_even = "odd" if Data.current_team == Data.teamA else "even"
        getrokken_ballen = [random.randint(0, 60) for _ in range(5)]  
        Data.current_team["kaart"] = mark_numbers_on_card(Data.current_team["kaart"], getrokken_ballen)
        display_bingokaart(Data.current_team["kaart"])
        switch_teams()
    else:
        switch_teams()
