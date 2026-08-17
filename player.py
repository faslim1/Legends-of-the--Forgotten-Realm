class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class

        self.level = 1
        self.exp = 0
        self.gold = 100

        self.weapon = None
        self.armor = None

        self.inventory = []
        self.potions = []

        self.bosses_defeated = []
        self.enemies_defeated = 0

        self.set_class_stats()

    def set_class_stats(self):

        if self.player_class == "Warrior":
            self.max_hp = 150
            self.max_mana = 50
            self.attack = 20
            self.defense = 15
            self.crit_chance = 5

        elif self.player_class == "Mage":
            self.max_hp = 100
            self.max_mana = 150
            self.attack = 25
            self.defense = 8
            self.crit_chance = 10

        elif self.player_class == "Archer":
            self.max_hp = 110
            self.max_mana = 100
            self.attack = 18
            self.defense = 10
            self.crit_chance = 15

        elif self.player_class == "Assassin":
            self.max_hp = 90
            self.max_mana = 100
            self.attack = 25
            self.defense = 7
            self.crit_chance = 25

        self.hp = self.max_hp
        self.mana = self.max_mana

        self.crit_damage = 1.5

    def show_stats(self):

        print("\n====== PLAYER STATS ======")
        print("Name:", self.name)
        print("Class:", self.player_class)
        print("Level:", self.level)
        print("EXP:", self.exp)

        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Mana: {self.mana}/{self.max_mana}")

        print("Attack:", self.attack)
        print("Defense:", self.defense)

        print("Critical Chance:", self.crit_chance, "%")
        print("Critical Damage:", self.crit_damage)

        print("Gold:", self.gold)

        print("Weapon:",
              self.weapon["name"] if self.weapon else "None")

        print("Armor:",
              self.armor["name"] if self.armor else "None")

        print("Enemies Defeated:", self.enemies_defeated)
        print("Bosses Defeated:", len(self.bosses_defeated))

