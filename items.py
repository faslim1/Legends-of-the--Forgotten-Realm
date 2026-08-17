import random

WEAPONS = [
    {"name": "Wooden Sword", "type": "weapon", "rank": "Common", "damage": 5, "crit": 0, "price": 50},
    {"name": "Iron Sword", "type": "weapon", "rank": "Rare", "damage": 12, "crit": 5, "price": 150},
    {"name": "Flame Sword", "type": "weapon", "rank": "Epic", "damage": 30, "crit": 12, "price": 500},
]

ARMORS = [
    {"name": "Leather Armor", "type": "armor", "rank": "Common", "defense": 3, "price": 50},
    {"name": "Iron Armor", "type": "armor", "rank": "Rare", "defense": 7, "price": 150},
    {"name": "Crystal Armor", "type": "armor", "rank": "Super Rare", "defense": 12, "price": 300},
]

POTIONS = [
    {"name": "Small Health Potion", "type": "potion", "effect": "health", "value": 50, "price": 20},
    {"name": "Medium Health Potion", "type": "potion", "effect": "health", "value": 100, "price": 40},
    {"name": "Large Health Potion", "type": "potion", "effect": "health", "value": 250, "price": 80},
]


def use_potion(player):
    potions = [item for item in player.inventory if item["type"] == "potion"]

    if not potions:
        print("You have no potions.")
        return False

    print("\n===== POTIONS =====")

    for number, potion in enumerate(potions, 1):
        print(f"{number}. {potion['name']}")

    try:
        choice = int(input("Choose potion: "))
        potion = potions[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return False

    if potion["effect"] == "health":
        old_hp = player.hp
        player.hp = min(player.max_hp, player.hp + potion["value"])
        print("HP restored:", player.hp - old_hp)

    elif potion["effect"] == "mana":
        old_mana = player.mana
        player.mana = min(player.max_mana, player.mana + potion["value"])
        print("Mana restored:", player.mana - old_mana)

    player.inventory.remove(potion)
    return True


def buy_item(player, items):
    print()

    for number, item in enumerate(items, 1):
        print(f"{number}. {item['name']} - {item['price']} Gold")

    try:
        choice = int(input("Choose item: "))
        item = items[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    if player.gold < item["price"]:
        print("Not enough gold.")
        return

    player.gold -= item["price"]
    player.inventory.append(item.copy())
    print(item["name"], "purchased!")


def shop(player):
    while True:
        print("\n===== VILLAGE SHOP =====")
        print("Gold:", player.gold)
        print("1. Buy Weapon")
        print("2. Buy Armor")
        print("3. Buy Potion")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            buy_item(player, WEAPONS)
        elif choice == "2":
            buy_item(player, ARMORS)
        elif choice == "3":
            buy_item(player, POTIONS)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


def drop_loot(player):
    chance = random.randint(1, 100)

    if chance <= 30:
        potion = random.choice(POTIONS)
        player.inventory.append(potion.copy())
        print("Loot:", potion["name"])

    elif chance <= 40:
        weapon = random.choice(WEAPONS[:3])
        player.inventory.append(weapon.copy())
        print("Loot:", weapon["name"])

    else:
        gold = random.randint(10, 40)
        player.gold += gold
        print("Loot:", gold, "Gold")