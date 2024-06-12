import pygame
import time
import sys
from Data import *
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
def soundplay(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()

def get_team_names():
    print(zinnen[0])
    team_1 = input(zinnen[1])
    team_2 = input(zinnen[2])
    team["team 1"] = team_1
    team["team 2"] = team_2
    teams.append(team)
    return teams
    


def get_random_word(woorden_lijst):
    te_raden = random.choice(words)
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
    beurt = 0
    attempts = [[te_raden[0]] + ["_"] * (len(te_raden) - 1)]
    display_grid(attempts, len(te_raden))

    
    while beurt <= 5:
        woord_invullen = input(zinnen[3])

        if woord_invullen == te_raden:
            print("\n" + termcolor.colored("Goed geraden!", 'green'))
            geraden_letters = [termcolor.colored(letter, 'green') for letter in te_raden]
            attempts.append(geraden_letters)
            display_grid(attempts, len(te_raden))
            return "goed geraden"
        
        geraden_letters = []
        empty_string = ""
        
        if len(set(woord_invullen)) == 1:
            print("Je invoer bevat alleen dezelfde letter. Voer een geldig woord in.")
            beurt += 1
            continue
        
        if len(woord_invullen) <5 or len(woord_invullen) >5:
            print(zinnen[13])
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
    return zinnen[6], te_raden



#added


def generate_bingokaart():
    bingokaart = []
    indiviuele_getallen = []
    getal = 0
    while getal < 16:
        random_getal = random.randint(0, 30)
        if random_getal not in indiviuele_getallen:  # Zorgt ervoor dat er geen dubbele getallen zijn in een rij
            getal += 1
            indiviuele_getallen.append(random_getal)
            if getal % 4 == 0:
                bingokaart.append(indiviuele_getallen)
                indiviuele_getallen = []
    return bingokaart

def display_bingokaart(bingokaart):
    print(tabulate(bingokaart, tablefmt="grid"))

#added