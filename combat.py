import random
from items import use_potion, drop_loot


SKILLS = {
    "Warrior": {"name": "Power Slash", "mana": 15, "damage": 1.8},
    "Mage": {"name": "Fireball", "mana": 20, "damage": 2.0},
    "Archer": {"name": "Multi Shot", "mana": 15, "damage": 1.7},
    "Assassin": {"name": "Backstab", "mana": 20, "damage": 2.2}
}


def player_attack(player, enemy):
    weapon_damage = 0
    weapon_crit = 0

    if player.weapon:
        weapon_damage = player.weapon["damage"]
        weapon_crit = player.weapon["crit"]

    damage = max(player.attack + weapon_damage - enemy.defense, 1)
    critical_chance = player.crit_chance + weapon_crit

    if random.randint(1, 100) <= critical_chance:
        damage = int(damage * player.crit_damage)
        print("*** CRITICAL HIT! ***")

    enemy.hp -= damage
    print("You dealt", damage, "damage.")


def use_skill(player, enemy):
    skill = SKILLS[player.player_class]

    print("\nSkill:", skill["name"])
    print("Mana Cost:", skill["mana"])

    if player.mana < skill["mana"]:
        print("Not enough mana.")
        return False

    player.mana -= skill["mana"]
    damage = max(int(player.attack * skill["damage"] - enemy.defense), 1)
    enemy.hp -= damage

    print(player.name, "used", skill["name"])
    print("Damage:", damage)

    return True


def enemy_attack(enemy, player, defending):
    armor_defense = player.armor["defense"] if player.armor else 0
    total_defense = player.defense + armor_defense
    damage = max(enemy.attack - total_defense, 1)

    if defending:
        damage = max(int(damage * 0.5), 1)
        print("Defense reduced the damage!")

    player.hp -= damage
    print(enemy.name, "dealt", damage, "damage.")


def battle(player, enemy):
    print("\n===== BATTLE =====")
    print("Enemy:", enemy.name)

    while player.hp > 0 and enemy.hp > 0:
        defending = False

        print("\n--------------------")
        print(f"{player.name}: {player.hp}/{player.max_hp} HP")
        print(f"{enemy.name}: {max(enemy.hp, 0)}/{enemy.max_hp} HP")
        print("\n1. Attack")
        print("2. Skill")
        print("3. Use Potion")
        print("4. Defend")
        print("5. View Stats")
        print("6. Run")

        choice = input("Choose action: ")

        if choice == "1":
            player_attack(player, enemy)

        elif choice == "2":
            if not use_skill(player, enemy):
                continue

        elif choice == "3":
            if not use_potion(player):
                continue

        elif choice == "4":
            defending = True
            print("You are defending.")

        elif choice == "5":
            player.show_stats()
            continue

        elif choice == "6":
            if enemy.boss:
                print("You cannot run from a boss.")
                continue

            if random.randint(1, 100) <= 50:
                print("You escaped.")
                return "escaped"

            print("Escape failed.")

        else:
            print("Invalid choice.")
            continue

        if enemy.hp <= 0:
            print("\nYou defeated", enemy.name)
            print("You received", enemy.gold_reward, "Gold.")

            player.gold += enemy.gold_reward
            player.gain_exp(enemy.exp_reward)
            player.enemies_defeated += 1

            if enemy.boss:
                player.bosses_defeated.append(enemy.name)
                print("BOSS DEFEATED!")

            drop_loot(player)
            return "victory"

        enemy_attack(enemy, player, defending)

    if player.hp <= 0:
        print("\n===== GAME OVER =====")
        return "defeat"