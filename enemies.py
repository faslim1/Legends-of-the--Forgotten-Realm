import random


class Enemy:
    def __init__(self, name, level, hp, attack, defense, exp, gold, boss=False):
        self.name = name
        self.level = level
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.exp_reward = exp
        self.gold_reward = gold
        self.boss = boss


ENEMY_NAMES = [
    "Goblin", "Wolf", "Slime", "Zombie", "Skeleton",
    "Orc", "Bandit", "Troll", "Dark Archer", "Giant Spider",
    "Vampire", "Werewolf", "Necromancer", "Ice Golem", "Fire Demon",
    "Desert Scorpion", "Dark Knight", "Lava Beast", "Ice Warrior", "Sky Guardian",
    "Demon Knight", "Dark Dragon", "Shadow Beast", "Ancient Warrior", "Demon Mage"
]

BOSSES = {
    10: "Goblin King",
    20: "Forest Guardian",
    30: "Ancient Golem",
    40: "Vampire Lord",
    50: "Dragon Rider",
    60: "Demon General",
    70: "Ice Titan",
    80: "Shadow Emperor",
    90: "Celestial Dragon",
    100: "Ancient Demon King"
}


def create_enemy(player_level):
    name = random.choice(ENEMY_NAMES)
    hp = 40 + player_level * 12
    attack = 5 + player_level * 2
    defense = 2 + player_level
    exp = 30 + player_level * 15
    gold = 10 + player_level * 5

    return Enemy(name, player_level, hp, attack, defense, exp, gold)


def create_boss(level):
    if level not in BOSSES:
        return None

    name = BOSSES[level]
    hp = 200 + level * 15
    attack = 15 + level * 2
    defense = 5 + level
    exp = level * 40
    gold = level * 20

    return Enemy(name, level, hp, attack, defense, exp, gold, True)