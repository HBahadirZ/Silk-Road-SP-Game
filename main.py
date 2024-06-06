from caravan_management import Caravan, EventSystem, Route, Member
from trading_system import Player, visit_market
from data import markets, goods, potential_members
import json
import random


def generate_potential_members():
    return random.sample(potential_members, 3)


def hire_member(caravan, available_members):
    print("\nAvailable Members for Hire:")
    for i, member in enumerate(available_members):
        print(
            f"{i + 1}. Name: {member.name}, Role: {member.role}, Health: {member.health}, Morale: {member.morale}, Skill Level: {member.skill_level}, Upfront Fee: {member.upfront_fee}, Wage: {member.wage}, Food Consumption: {member.food_consumption}, Water Consumption: {member.water_consumption}"
        )

    choice = int(input("Select a member to hire (1-3): ").strip()) - 1
    if 0 <= choice < len(available_members):
        selected_member = available_members[choice]
        if caravan.resources.money >= selected_member.upfront_fee:
            caravan.resources.money -= selected_member.upfront_fee
            caravan.add_member(selected_member)
            print(f"{selected_member.name} hired!")
        else:
            print("Not enough money to hire this member.")
    else:
        print("Invalid choice. Please try again.")


def manage_caravan(caravan):
    print("\nCaravan Status:")
    caravan.display_caravan()
    print("\n1. Add Member")
    print("2. Remove Member")
    print("3. Return to Main Menu")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        available_members = generate_potential_members()
        hire_member(caravan, available_members)
    elif choice == "2":
        name = input("Enter the name of the member to remove: ").strip()
        caravan.remove_member(name)
        print(f"Member {name} removed.")
    elif choice == "3":
        return
    else:
        print("Invalid choice. Please try again.")


def update_daily_consumption(caravan):
    daily_food_consumption = sum(member.food_consumption
                                 for member in caravan.members)
    daily_water_consumption = sum(member.water_consumption
                                  for member in caravan.members)
    caravan.resources.food -= daily_food_consumption
    caravan.resources.water -= daily_water_consumption
    if caravan.resources.food <= 0:
        for member in caravan.members:
            member.update_morale(-25)  # Decrease morale if no food
    if caravan.resources.water <= 0:
        for member in caravan.members:
            member.update_morale(-25)  # Decrease morale if no water


def pay_wages(caravan):
    total_wages = sum(member.wage for member in caravan.members)
    if caravan.resources.money >= total_wages:
        caravan.resources.money -= total_wages
        print(f"Paid {total_wages} in wages.")
    else:
        print(
            "Not enough money to pay wages. Members may leave or suffer penalties."
        )
        for member in caravan.members:
            member.update_morale(-50)  # Decrease morale if wages are not paid


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
        update_daily_consumption(caravan)
        caravan.check_members()
        caravan.display_caravan()
    pay_wages(caravan)  # Pay wages at the end of the travel


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
                'morale': member.morale,
                'skill_level': member.skill_level,
                'upfront_fee': member.upfront_fee,
                'wage': member.wage,
                'food_consumption': member.food_consumption,
                'water_consumption': member.water_consumption
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
                   morale=member['morale'],
                   skill_level=member['skill_level'],
                   upfront_fee=member['upfront_fee'],
                   wage=member['wage'],
                   food_consumption=member['food_consumption'],
                   water_consumption=member['water_consumption'])
            for member in game_state['caravan']['members']
        ]
        print("Game loaded successfully.")
    except FileNotFoundError:
        print("No saved game found.")


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
            visit_market(player, market_name)
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
