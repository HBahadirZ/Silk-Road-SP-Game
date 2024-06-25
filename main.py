from caravan_management import Caravan, EventSystem, Route, Member
from trading_system import Player, visit_market
from data import markets, goods, potential_members
import json
import random

available_members = []  # Global list to track currently available members

can_hire_members = False


def generate_potential_members(number_of_members):
    global available_members
    available_members = random.sample(potential_members, number_of_members)


def initial_hiring(caravan):
    global available_members
    print("\nInitial Members for Hire:")
    for i, member in enumerate(available_members):
        print(
            f"{i + 1}. {member.name}, Role: {member.role}, Skill Level: {member.skill_level}, Upfront Fee: {member.upfront_fee}, Wage: {member.wage}"
        )

    hired_members = 0
    while hired_members < 3:
        try:
            choice = int(
                input(
                    f"Select a member to hire (you need to hire {3 - hired_members} more) (enter number): "
                ).strip()) - 1
            if 0 <= choice < len(available_members):
                member = available_members[choice]
                if caravan.resources.money >= member.upfront_fee:
                    available_members.pop(choice)
                    caravan.add_member(member)
                    caravan.resources.money -= member.upfront_fee
                    print(f"Hired {member.name} as {member.role}.")
                    hired_members += 1
                else:
                    print("Not enough money to hire this member.")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def hire_member(caravan):
    global can_hire_members, available_members

    if not can_hire_members:
        print("You cannot hire members until you travel to another city.")
        return

    if not available_members:
        print(
            "No available members to hire. Please travel to another city to find new members."
        )
        return

    print("\nAvailable Members for Hire:")
    for i, member in enumerate(available_members):
        print(
            f"{i + 1}. {member.name}, Role: {member.role}, Skill Level: {member.skill_level}, Upfront Fee: {member.upfront_fee}, Wage: {member.wage}"
        )

    try:
        choice = int(
            input("Select a member to hire (enter number): ").strip()) - 1
        if 0 <= choice < len(available_members):
            member = available_members.pop(choice)
            caravan.add_member(member)
            print(f"Hired {member.name} as {member.role}.")
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def manage_caravan(caravan):
    print("\nCaravan Status:")
    caravan.display_caravan()
    print("\n1. Add Member")
    print("2. Remove Member")
    print("3. Return to Main Menu")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        hire_member(caravan)
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


def reset_available_members():
    global can_hire_members
    generate_potential_members(3)  # Generate new potential members
    can_hire_members = True


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
        reset_available_members()  # Reset available members after travel
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

        # Wait for user input to continue to the next day
        while True:
            cont = input("Press 'c' to continue to the next day: ")
            if cont:
                break
            else:
                print("Invalid input. Please press 'c' to continue.")

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
    global can_hire_members
    caravan = Caravan()  # Create a new caravan instance
    player = Player(caravan)  # Link the player to the caravan
    event_system = EventSystem()  # Initialize the event system
    generate_potential_members(5)
    initial_hiring(caravan)
    can_hire_members = False
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
