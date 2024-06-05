import pygame
import time
import sys
from Data import *
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


def play_lingo(te_raden):
    beurt = 0
    print("Te raden woord:", te_raden[0] + "_" * (len(te_raden) - 1))
    print(f"het woord is {te_raden}")
    
    while beurt <= 5:
        woord_invullen = input(zinnen[3])
                    
        if woord_invullen == te_raden:
            return "goed geraden"
        
        geraden_letters = []
        empty_string = ""
        
        if len(set(woord_invullen)) == 1:
            print("Je invoer bevat alleen dezelfde letter. Voer een geldig woord in.")
            beurt += 1
            continue
        
        else:
            for i, letter in enumerate(woord_invullen):
                
            
                
                if letter == te_raden[i]:
                    geraden_letters.append(letter)
                    empty_string += termcolor.colored(letter, 'green') + " "
                    

                    
                elif letter in te_raden:
                    geraden_letters.append("_")
                    empty_string += termcolor.colored(letter, 'yellow') + " "
                    
            
                    
                else:
                    geraden_letters.append("_")
                    empty_string += letter + " "
                    
            beurt += 1     
            print("Geraden woord:", " ".join(geraden_letters))
            print(empty_string)
            
    return zinnen[6] , te_raden



# dit had ik eerst 
# def play_lingo(te_raden):
#     beurt = 0
#     print(te_raden) # for debugging
#     print(te_raden[0] + "_" * (len(te_raden) - 1))

#     while beurt <= 5:
#         woord_invullen = input(zinnen[3])
#         if woord_invullen in te_raden:
#             return "goed geraden"
            
#         for pos , letter in enumerate(te_raden):
#             if letter == woord_invullen:
                
#                 te_raden[pos] = letter
#             # elif x in te_raden and pos != te_raden:
#             #     return "letter zit in het woord"
            
#             # else:
#             #     beurt += 1
#             #     return "fout"