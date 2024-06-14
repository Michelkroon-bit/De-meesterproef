import pygame
import time
import sys
import Data
import string
import random
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
    
    beurt = 0
    attempts = [[te_raden[0]] + ["_"] * (len(te_raden) - 1)]
    display_grid(attempts, len(te_raden))

    while beurt < 5:
        woord_invullen = input(Data.zinnen[3])
        result = check_for_conditions(woord_invullen, te_raden, attempts)
        if result == "goed geraden":
            return result, te_raden
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


def grab_bal():
    ballenbak = Data.ballen_even + Data.ballen_odd + Data.speciale_ballen
    nummers = [bal for bal in ballenbak if isinstance(bal, int)]
    even_nummers = [bal for bal in nummers if bal % 2 == 0]
    oneven_nummers = [bal for bal in nummers if bal % 2 != 0]

    getrokken_ballen = []
    for _ in range(2):  # Trek twee keer een bal
        if Data.current_team["even_or_odd"] == "odd":
            if oneven_nummers:
                nummer = random.choice(oneven_nummers)
                getrokken_ballen.append(nummer)
                ballenbak.remove(nummer)
        else:
            if even_nummers:
                nummer = random.choice(even_nummers)
                getrokken_ballen.append(nummer)
                ballenbak.remove(nummer)
    return getrokken_ballen



def bingo_turn(team_name, kaart):
    print(f"Het is {Data.current_team['name']}`s beurt!")
    
    if Data.current_team["even_or_odd"] == "odd":
        ballenlijst = Data.ballen_odd
    elif Data.current_team["even_or_odd"] == "even":
        ballenlijst = Data.ballen_even

    getrokken_ballen = grab_bal()
    print(f"{Data.current_team['name']} heeft balnummer {getrokken_ballen[0]} en {getrokken_ballen[1]} getrokken.")

def mark_numbers_on_card(kaart, getrokken_ballen):
    for nummer in getrokken_ballen:
        for rij in kaart:
            for i in range(len(rij)):
                if rij[i] == nummer:
                    rij[i] = colored("X", 'red')
    return kaart