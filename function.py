import pygame
import time
import sys
from Data import *
import string
import random
import termcolor


def typemachine_print (prompt):
    for x in prompt:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.25)
        
    return prompt
def soundplay(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()

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
    attempts = []
    print("Te raden woord:", te_raden[0] + "_" * (len(te_raden) - 1))
    print(f"het woord is {te_raden}")
    
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

        else:
            for i, letter in enumerate(woord_invullen):
                
                
                if letter not in string.ascii_lowercase:
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



"""

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
    attempts = []
    print("Te raden woord:", te_raden[0] + "_" * (len(te_raden) - 1))
    print(f"het woord is {te_raden}")

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

        for i, letter in enumerate(woord_invullen):
            
            if letter not in string.ascii_lowercase:
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

# Example usage:
# te_raden = "example"
# zinnen = ["Prompt", "Another Prompt", "Yet Another Prompt", "Raad het woord: ", "More prompts", "Another one", "Je hebt verloren!"]
play_lingo("tafel")
"""