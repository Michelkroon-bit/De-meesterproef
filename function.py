import pygame
import time
import sys
import Data   
import string
import random
import termcolor
from tabulate import tabulate

def typemachine_print (prompt , speed):
    for x in prompt:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(speed)
        
    return prompt

def switch_teams():
    if Data.current_team == Data.teamA:
        Data.teamA = Data.current_team
        Data.current_team = Data.teamB
    else:
        Data.teamB = Data.current_team
        Data.current_team = Data.teamA

def get_team_data(team):
    print(team)   

def get_random_word(woorden_lijst):
    te_raden = random.choice(Data.words)
    return te_raden


def display_grid(attempts, te_raden_length):
    grid_size = te_raden_length
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

    
    while beurt <= 5:
        woord_invullen = input(Data.zinnen[3])

        if woord_invullen == te_raden:
            print("\n" + termcolor.colored("Goed geraden!", 'green'))
            geraden_letters = [termcolor.colored(letter, 'green') for letter in te_raden]
            attempts.append(geraden_letters)
            display_grid(attempts, len(te_raden))
            Data.current_team["correct_words"] +=1
            return "goed geraden"
        
        geraden_letters = []
        empty_string = ""
        
        if len(set(woord_invullen)) == 1:
            print("Je invoer bevat alleen dezelfde letter. Voer een geldig woord in.")
            beurt += 1
            continue
        
        if len(woord_invullen) <5 or len(woord_invullen) >5:
            print(Data.zinnen[13])
            beurt +=1
            continue
            
        else:
            for i, letter in enumerate(woord_invullen):
                
                
                if letter not in string.ascii_lowercase or letter == "":
                    print("FOUTE INPUT!! alleen letters zijn toegestaan")
                    geraden_letters = [te_raden[0]] + ["_"] * (len(te_raden) - 1)
                    empty_string = woord_invullen
                    beurt += 1
                    break
                    
                if letter == te_raden[i]:
                    geraden_letters.append(termcolor.colored(letter, 'green'))

                
                elif letter in te_raden:
                    geraden_letters.append(termcolor.colored(letter, 'yellow'))
                
                else:
                    geraden_letters.append(letter)
            
        attempts.append(geraden_letters)
        display_grid(attempts, len(te_raden))
        beurt += 1


    print("\n" + termcolor.colored("Helaas, je hebt het woord niet geraden.", 'red'))
    print(f"Het juiste woord was: {te_raden}")
    return Data.zinnen[6], te_raden



#added
def generate_bingokaart(odd_or_even):
    
    if odd_or_even == "odd":
        bingokaart = []
        indiviuele_getallen = []
        getal = 0
        while getal < 16:
            random_getal = random.choice(Data.ballen_odd)
            if random_getal not in indiviuele_getallen:  # Zorgt ervoor dat er geen dubbele getallen zijn in een rij
                getal += 1
                indiviuele_getallen.append(random_getal)
                if getal % 4 == 0:
                    bingokaart.append(indiviuele_getallen)
                    indiviuele_getallen = []
        return bingokaart
    
    else:
        bingokaart = []
        indiviuele_getallen = []
        getal = 0
        while getal < 16:
            random_getal = random.randint(Data.ballen_even)
            if random_getal not in indiviuele_getallen:  # Zorgt ervoor dat er geen dubbele getallen zijn in een rij
                getal += 1
                indiviuele_getallen.append(random_getal)
                if getal % 4 == 0:
                    bingokaart.append(indiviuele_getallen)
                    indiviuele_getallen = []
        return bingokaart

def display_bingokaart(bingokaart):
    print(tabulate(bingokaart, tablefmt="grid"))