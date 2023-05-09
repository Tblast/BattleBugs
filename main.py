import random
from random import choice

monster = {
    "name": "Killer Mantis",
    "hp": 10,
    "attacks": {
        "weak": {
            "to_hit": .8,
            "damage": range(1, 4),

        },
        "strong": {
            "to_hit": .4,
            "damage": range(3, 8),
        }
    }
}

player = {
    "name": "Ant Boy",
    "hp": 20,
    "attacks": {
        "weak": {
            "to_hit": .8,
            "damage": range(1, 4),

        },
        "strong": {
            "to_hit": .4,
            "damage": range(3, 8),
        }
    }
}


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
