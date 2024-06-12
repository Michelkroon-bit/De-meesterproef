# import random
# from tabulate import tabulate

# def generate_bingokaart():
#     bingokaart = []
#     indiviuele_getallen = []
#     getal = 0
#     while getal < 16:
#         random_getal = random.randint(1, 30)
#         if random_getal not in indiviuele_getallen:
#             getal += 1
#             indiviuele_getallen.append(random_getal)
#             if getal % 4 == 0:
#                 bingokaart.append(indiviuele_getallen)
#                 indiviuele_getallen = []
#     return bingokaart

# def display_bingokaart(bingokaart):
#     print(tabulate(bingokaart, tablefmt="grid"))

# def bingo_turn(team_name, kaart, ballenbak):
#     print(f"{team_name}'s beurt!")
#     display_bingokaart(kaart)
#     nummer = grab_bal(ballenbak, team_name)
#     print(f"{team_name} heeft balnummer {nummer} getrokken.")
#     for rij in kaart:
#         if nummer in rij:
#             rij[rij.index(nummer)] = "●"
#     display_bingokaart(kaart)
#     return kaart

# def grab_bal(ballenbak, team_name):
#     nummers = [bal for bal in ballenbak if isinstance(bal, int)]
#     even_nummers = [bal for bal in nummers if bal % 2 == 0]
#     oneven_nummers = [bal for bal in nummers if bal % 2 != 0]
#     if team_name == "team 1":
#         nummer = random.choice(even_nummers)
#     else:
#         nummer = random.choice(oneven_nummers)
#     ballenbak.remove(nummer)
#     return nummer


# def check_bingo(kaart):
#     for rij in kaart:
#         if all(item == "X" for item in rij):
#             return True
#     for col in range(4):
#         if all(row[col] == "X" for row in kaart):
#             return True
#     return False

# def main_bingo():
#     team_names = {"team 1": "Team 1", "team 2": "Team 2"}  # Verander de namen van de teams indien nodig
#     kaarten = {team: generate_bingokaart() for team in team_names}
#     ballenbak = list(range(1, 31))
#     ballenbak.extend(["groen", "groen", "groen", "rood", "rood", "rood"])  # Groene en rode ballen toevoegen

#     while True:
#         for team_name, team_display in team_names.items():
#             input(f"Druk op Enter voor de beurt van {team_display}...")
#             print("\n" + "="*20)
#             kaarten[team_name] = bingo_turn(team_display, kaarten[team_name], ballenbak)
#             if check_bingo(kaarten[team_name]):
#                 print(f"\n{team_display} heeft BINGO!")
#                 return

# if __name__ == "__main__":
#     main_bingo()
















abc = 0
















def blaat ():
    
    return "team1"

def blaat2():
    abc = blaat()
    return abc

abcd = blaat2()
print(abcd)