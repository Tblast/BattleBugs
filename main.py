import json
import random
from random import choice

with open('player.json', 'r') as f:
    player = json.load(f)

with open('monster.json', 'r') as f:
    monster = json.load(f)

def fight(p1, p2):
    while all([p1["hp"], p2["hp"]]) > 0:
        print("Fight round commences")
        p1_damage = choice(p1['attacks']['weak']['damage'])
        p2_damage = choice(p2['attacks']['weak']['damage'])
        print(f"{p1['name']} attacks for {p1_damage}")
        print(f"{p2['name']} attacks for {p2_damage}")
        p1["hp"] -= p2_damage
        p2["hp"] -= p1_damage
    print(f"{p1['name'] if p1['hp'] < 0 else p2['name']} has succumbed to the blade.")


def main():
    print("in the main function")
    fight(player, monster)


if __name__ == "__main__":
    print("caught the terminal call")
    main()
