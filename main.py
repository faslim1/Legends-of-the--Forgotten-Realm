from player import create_player
from enemies import create_enemy, create_boss, BOSSES
from combat import battle
from items import shop
from save_load import save_game, load_game


REGIONS = [
    "Village",
    "Forest",
    "Cave",
    "Desert",
    "Ruins",
    "Castle",
    "Volcano",
    "Frozen Mountain",
    "Sky Temple",
    "Demon Realm"
]


def show_world(player):
    region_number = min((player.level - 1) // 10, len(REGIONS) - 1)

    print("\n===== WORLD MAP =====")

    for number, region in enumerate(REGIONS):
        if number == region_number:
            print("->", region, "<-")
        else:
            print(region)

    print("Current Region:", REGIONS[region_number])


def inventory_menu(player):
    while True:
        player.show_inventory()

        if not player.inventory:
            return

        print("\nEnter item number to equip.")
        print("0. Return")

        try:
            choice = int(input("Choice: "))

            if choice == 0:
                return

            item = player.inventory[choice - 1]

            if item["type"] in ["weapon", "armor"]:
                player.equip_item(item)

            elif item["type"] == "potion":
                print("Potions can be used during battle.")

        except (ValueError, IndexError):
            print("Invalid choice.")


def victory_screen(player):
    print("\n==========================")
    print("VICTORY!")
    print("==========================")
    print("The Ancient Demon King has been defeated!")
    print("Peace has returned to Eldoria.")
    print("\n===== FINAL STATS =====")
    print("Player:", player.name)
    print("Class:", player.player_class)
    print("Final Level:", player.level)
    print("Gold:", player.gold)
    print("Enemies Defeated:", player.enemies_defeated)
    print("Bosses Defeated:", len(player.bosses_defeated))


def game_loop(player):
    while True:
        print("\n==============================")
        print("LEGENDS OF THE FORGOTTEN REALM")
        print("==============================")
        print(f"{player.name} | Level {player.level}")
        print(f"HP: {player.hp}/{player.max_hp}")
        print("Gold:", player.gold)

        print("\n1. Explore")
        print("2. View Stats")
        print("3. Inventory")
        print("4. Shop")
        print("5. World Map")
        print("6. Rest")
        print("7. Save Game")
        print("8. Exit to Main Menu")

        choice = input("Choose option: ")

        if choice == "1":
            if player.level in BOSSES:
                boss = create_boss(player.level)

                if boss.name not in player.bosses_defeated:
                    print("\nA BOSS HAS APPEARED!")
                    result = battle(player, boss)

                    if result == "defeat":
                        return

                    if boss.name == "Ancient Demon King" and result == "victory":
                        victory_screen(player)
                        return

                    continue

            enemy = create_enemy(player.level)
            result = battle(player, enemy)

            if result == "defeat":
                return

        elif choice == "2":
            player.show_stats()

        elif choice == "3":
            inventory_menu(player)

        elif choice == "4":
            shop(player)

        elif choice == "5":
            show_world(player)

        elif choice == "6":
            player.hp = player.max_hp
            player.mana = player.max_mana
            print("HP and Mana fully restored.")

        elif choice == "7":
            save_game(player)

        elif choice == "8":
            return

        else:
            print("Invalid option.")


def instructions():
    print("\n===== INSTRUCTIONS =====")
    print("1. Explore and fight enemies.")
    print("2. Gain EXP and Gold.")
    print("3. Buy weapons, armor and potions.")
    print("4. Equip better weapons and armor.")
    print("5. Defeat bosses.")
    print("6. Reach Level 100.")
    print("7. Defeat the Ancient Demon King.")


def main():
    while True:
        print("\n=============================")
        print("LEGENDS OF THE FORGOTTEN REALM")
        print("=============================")
        print("1. New Game")
        print("2. Continue")
        print("3. Instructions")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            player = create_player()
            game_loop(player)

        elif choice == "2":
            player = load_game()

            if player:
                game_loop(player)

        elif choice == "3":
            instructions()

        elif choice == "4":
            print("Thanks for playing!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()