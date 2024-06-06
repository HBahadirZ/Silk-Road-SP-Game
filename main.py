from caravan_management import Caravan, EventSystem, Route, Member
from trading_system import Player, visit_market, markets, goods
import json


def travel(caravan, event_system):
    routes = [
        Route(name="Desert Path",
              length=10,
              danger_level=5,
              rewards="Rich Trade Opportunities"),
        Route(name="Mountain Pass",
              length=15,
              danger_level=7,
              rewards="Rare Goods"),
        Route(name="Coastal Road",
              length=8,
              danger_level=3,
              rewards="Common Goods"),
    ]

    print("Available Routes:")
    for i, route in enumerate(routes):
        print(
            f"{i + 1}. {route.name} (Length: {route.length}, Danger Level: {route.danger_level}, Rewards: {route.rewards})"
        )

    choice = int(input("Select a route: ").strip()) - 1

    if 0 <= choice < len(routes):
        selected_route = routes[choice]
        selected_route.display_route()
        simulate_travel(caravan, selected_route, event_system)
    else:
        print("Invalid choice. Please try again.")


def simulate_travel(caravan, route, event_system):
    for day in range(route.length):
        print(f"\nDay {day + 1}:")
        event = event_system.generate_event()
        event_system.resolve_event(event, caravan)
        caravan.display_caravan()


def save_game(player, caravan):
    game_state = {
        'player': {
            'goods': player.goods,
            'currencies': player.currencies,
        },
        'caravan': {
            'resources': {
                'food': caravan.resources.food,
                'water': caravan.resources.water,
                'money': caravan.resources.money,
            },
            'members': [{
                'name': member.name,
                'role': member.role,
                'health': member.health,
                'skill_level': member.skill_level
            } for member in caravan.members],
        },
    }

    with open('savegame.json', 'w') as f:
        json.dump(game_state, f)
    print("Game saved successfully.")


def load_game(player, caravan):
    try:
        with open('savegame.json', 'r') as f:
            game_state = json.load(f)

        player.goods = game_state['player']['goods']
        player.currencies = game_state['player']['currencies']

        caravan.resources.food = game_state['caravan']['resources']['food']
        caravan.resources.water = game_state['caravan']['resources']['water']
        caravan.resources.money = game_state['caravan']['resources']['money']
        caravan.members = [
            Member(name=member['name'],
                   role=member['role'],
                   health=member['health'],
                   skill_level=member['skill_level'])
            for member in game_state['caravan']['members']
        ]
        print("Game loaded successfully.")
    except FileNotFoundError:
        print("No saved game found.")


def manage_caravan(caravan):
    print("\nCaravan Status:")
    caravan.display_caravan()
    print("\n1. Add Member")
    print("2. Remove Member")
    print("3. Return to Main Menu")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        name = input("Enter the name of the new member: ").strip()
        role = input(
            "Enter the role of the new member (Guard, Merchant, Scout, Healer): "
        ).strip()
        health = int(
            input("Enter the health of the new member (0-100): ").strip())
        skill_level = int(
            input("Enter the skill level of the new member (1-10): ").strip())
        new_member = Member(name=name,
                            role=role,
                            health=health,
                            skill_level=skill_level)
        caravan.add_member(new_member)
        print(f"Member {name} added.")
    elif choice == "2":
        name = input("Enter the name of the member to remove: ").strip()
        caravan.remove_member(name)
        print(f"Member {name} removed.")
    elif choice == "3":
        return
    else:
        print("Invalid choice. Please try again.")


def main():
    caravan = Caravan()  # Create a new caravan instance
    player = Player(caravan)  # Link the player to the caravan
    event_system = EventSystem()  # Initialize the event system

    while True:
        print("\nMain Menu:")
        print("1. Travel to a Market")
        print("2. Trade Goods")
        print("3. Manage Caravan")
        print("4. Save Game")
        print("5. Load Game")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            travel(caravan, event_system)
        elif choice == "2":
            market_name = input("Enter the market you want to visit: ").strip()
            if market_name in markets:
                visit_market(player, market_name)
            else:
                print("Invalid market. Please try again.")
        elif choice == "3":
            manage_caravan(caravan)
        elif choice == "4":
            save_game(player, caravan)
        elif choice == "5":
            load_game(player, caravan)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
