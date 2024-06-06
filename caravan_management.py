import random


# Caravan Resources
class CaravanResources:

    def __init__(self, food, water, money):
        self.food = food
        self.water = water
        self.money = money

    def update_resource(self, resource, amount):
        if resource in self.__dict__:
            self.__dict__[resource] += amount
            if self.__dict__[resource] < 0:
                self.__dict__[resource] = 0

    def display_resources(self):
        print(f"Food: {self.food}, Water: {self.water}, Money: {self.money}")


# Member Class
class Member:

    def __init__(self, name, role, health, skill_level, upfront_fee, wage,
                 food_consumption, water_consumption):
        self.name = name
        self.role = role
        self.health = health
        self.skill_level = skill_level
        self.upfront_fee = upfront_fee
        self.wage = wage
        self.food_consumption = food_consumption
        self.water_consumption = water_consumption
        self.morale = 100  # Initialize morale at 100

    def update_health(self, amount):
        self.health += amount
        if self.health < 0:
            self.health = 0
        elif self.health > 100:
            self.health = 100
        self.update_morale(amount)  # Decrease morale if health decreases

    def update_morale(self, amount):
        self.morale += amount
        if self.morale < 0:
            self.morale = 0
        elif self.morale > 100:
            self.morale = 100

    def display_member(self):
        print(
            f"Name: {self.name}, Role: {self.role}, Health: {self.health}, Morale: {self.morale}, Skill Level: {self.skill_level}, Upfront Fee: {self.upfront_fee}, Wage: {self.wage}, Food Consumption: {self.food_consumption}, Water Consumption: {self.water_consumption}"
        )


# Caravan Class
class Caravan:

    def __init__(self):
        self.resources = CaravanResources(food=100, water=100, money=500)
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_name):
        self.members = [
            member for member in self.members if member.name != member_name
        ]

    def update_resources(self, resource, amount):
        self.resources.update_resource(resource, amount)

    def display_caravan(self):
        self.resources.display_resources()
        for member in self.members:
            member.display_member()

    def check_members(self):
        members_to_remove = [
            member.name for member in self.members
            if member.health == 0 or member.morale == 0
        ]
        for member_name in members_to_remove:
            print(
                f"{member_name} has left the caravan due to low health or morale."
            )
            self.remove_member(member_name)


# Route Class
class Route:

    def __init__(self, name, length, danger_level, rewards):
        self.name = name
        self.length = length
        self.danger_level = danger_level
        self.rewards = rewards

    def display_route(self):
        print(
            f"Route: {self.name}, Length: {self.length}, Danger Level: {self.danger_level}, Rewards: {self.rewards}"
        )


# Enhanced Event System
class EventSystem:

    def __init__(self):
        self.events = [
            {
                "type": "bandit_attack",
                "description": "Bandits are attacking!",
                "impact": self.bandit_attack
            },
            {
                "type": "illness_outbreak",
                "description": "An illness is spreading among the caravan.",
                "impact": self.illness_outbreak
            },
            {
                "type": "natural_disaster",
                "description": "A sandstorm hits the caravan.",
                "impact": self.natural_disaster
            },
            {
                "type": "good_weather",
                "description": "Good weather speeds up the journey.",
                "impact": self.good_weather
            },
            {
                "type": "trader_help",
                "description": "A friendly trader offers assistance.",
                "impact": self.trader_help
            },
            {
                "type": "find_oasis",
                "description": "You find an oasis!",
                "impact": self.find_oasis
            },
            {
                "type": "broken_wheel",
                "description": "A wheel on a wagon breaks.",
                "impact": self.broken_wheel
            },
            {
                "type": "caravan_festival",
                "description": "A nearby caravan invites you to a festival.",
                "impact": self.caravan_festival
            },
        ]

    def generate_event(self):
        return random.choice(self.events)

    def resolve_event(self, event, caravan):
        print(event["description"])
        event["impact"](caravan)

    # Event Handlers
    def bandit_attack(self, caravan):
        loss_food = random.randint(5, 20)
        loss_money = random.randint(10, 50)
        damage_health = random.randint(10, 30)
        caravan.update_resources('food', -loss_food)
        caravan.update_resources('money', -loss_money)
        for member in caravan.members:
            member.update_health(-damage_health)
        print(
            f"Lost {loss_food} food, {loss_money} money, and members took {damage_health} damage each."
        )

    def illness_outbreak(self, caravan):
        loss_water = random.randint(5, 15)
        damage_health = random.randint(5, 20)
        caravan.update_resources('water', -loss_water)
        for member in caravan.members:
            member.update_health(-damage_health)
        print(
            f"Lost {loss_water} water and members took {damage_health} damage each."
        )

    def natural_disaster(self, caravan):
        loss_water = random.randint(10, 30)
        loss_food = random.randint(10, 30)
        damage_health = random.randint(10, 25)
        caravan.update_resources('water', -loss_water)
        caravan.update_resources('food', -loss_food)
        for member in caravan.members:
            member.update_health(-damage_health)
        print(
            f"Lost {loss_water} water, {loss_food} food, and members took {damage_health} damage each."
        )

    def good_weather(self, caravan):
        print("Good weather shortens the journey by one day.")

    def trader_help(self, caravan):
        gain_food = random.randint(10, 30)
        gain_water = random.randint(10, 30)
        caravan.update_resources('food', gain_food)
        caravan.update_resources('water', gain_water)
        print(f"Gained {gain_food} food and {gain_water} water.")

    def find_oasis(self, caravan):
        gain_water = random.randint(20, 50)
        caravan.update_resources('water', gain_water)
        print(f"Gained {gain_water} water from the oasis.")

    def broken_wheel(self, caravan):
        cost_money = random.randint(20, 50)
        caravan.update_resources('money', -cost_money)
        print(f"Spent {cost_money} money to repair the broken wheel.")

    def caravan_festival(self, caravan):
        gain_morale = random.randint(10, 30)
        for member in caravan.members:
            member.update_health(gain_morale)
        print(f"Members gained {gain_morale} health from the festival.")
