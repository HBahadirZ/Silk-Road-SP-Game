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

    def add_bulk_resources(self, food=0, water=0, money=0):
        self.food += food
        self.water += water
        self.money += money
        self.validate_resources()

    def validate_resources(self):
        self.food = max(0, self.food)
        self.water = max(0, self.water)
        self.money = max(0, self.money)

    def display_resources(self):
        print(f"Food: {self.food}, Water: {self.water}, Money: {self.money}")


# Member Class
class Member:

    def __init__(self,
                 name,
                 role,
                 health,
                 skill_level,
                 upfront_fee,
                 wage,
                 food_consumption,
                 water_consumption,
                 morale=100):
        self.name = name
        self.role = role
        self.health = health
        self.skill_level = skill_level
        self.upfront_fee = upfront_fee
        self.wage = wage
        self.food_consumption = food_consumption
        self.water_consumption = water_consumption
        self.morale = morale  # Initialize morale attribute
        self.traits = []

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

    def add_trait(self, trait):
        self.traits.append(trait)

    def display_member(self):
        traits_str = ", ".join(self.traits)
        print(
            f"Name: {self.name}, Role: {self.role}, Health: {self.health}, Morale: {self.morale}, Skill Level: {self.skill_level}, Upfront Fee: {self.upfront_fee}, Wage: {self.wage}, Food Consumption: {self.food_consumption}, Water Consumption: {self.water_consumption}, Traits: {traits_str}"
        )


# Caravan Class
class Caravan:

    def __init__(self):
        self.resources = CaravanResources(food=100, water=100, money=750)
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_name):
        self.members = [
            member for member in self.members if member.name != member_name
        ]

    def update_resources(self, resource, amount):
        self.resources.update_resource(resource, amount)

    def update_members_health(self, amount):
        for member in self.members:
            member.update_health(amount)

    def update_members_morale(self, amount):
        for member in self.members:
            member.update_morale(amount)

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

    def __init__(self, name, length, danger_level, rewards, hazards=None):
        self.name = name
        self.length = length
        self.danger_level = danger_level
        self.rewards = rewards
        self.hazards = hazards if hazards else []

    def display_route(self):
        hazards_str = ", ".join(self.hazards)
        print(
            f"Route: {self.name}, Length: {self.length}, Danger Level: {self.danger_level}, Rewards: {self.rewards}, Hazards: {hazards_str}"
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
        bandit_power = random.randint(50, 150)
        member_power = sum(member.skill_level for member in caravan.members)

        print(
            f"Bandits' Power: {bandit_power}, Members' Power: {member_power}")

        if bandit_power > 1.5 * member_power:
            # Scenario 1: Bandits kill all members and take half the money
            caravan.members.clear()
            caravan.update_resources('money', -caravan.resources.money // 2)
            if not caravan.members:
                print(
                    "Bandits took all the money as there were no one to protect your money."
                )
                caravan.update_resources('money', -caravan.resources.money)
            else:
                print(
                    "Bandits were much more powerful! All members are killed and half the money is stolen."
                )
        elif bandit_power > member_power:
            # Scenario 2: Bandits kill one member randomly and take 25% of the money
            if caravan.members:
                killed_member = random.choice(caravan.members)
                caravan.remove_member(killed_member.name)
                print(
                    f"Bandits were slightly more powerful! {killed_member.name} is killed."
                )
            caravan.update_resources('money', -caravan.resources.money // 4)
            print("25% of the money is stolen.")
        elif member_power > bandit_power:
            if member_power > 1.5 * bandit_power:
                # Scenario 4: Members are much more powerful, no harm
                print(
                    "Members were much more powerful! No harm to the caravan.")
            else:
                # Scenario 3: Members' health decreases a little
                damage_health = random.randint(5, 15)
                for member in caravan.members:
                    member.update_health(-damage_health)
                print(
                    f"Members were slightly more powerful! Each member took {damage_health} damage."
                )
        else:
            # Default case (should not be reached)
            print("Unexpected outcome in bandit attack.")

    def illness_outbreak(self, caravan):
        if not caravan.members:
            print(
                "There are no members in the caravan to be affected by the illness."
            )
            return

        illness_power = random.randint(5, 30)
        num_affected_members = random.randint(1, len(caravan.members))

        affected_members = random.sample(caravan.members, num_affected_members)
        print(f"Illness Power: {illness_power}")

        for member in affected_members:
            member.update_health(-illness_power)
            print(
                f"{member.name} was affected by the illness and lost {illness_power} health."
            )

        if not affected_members:
            print("No members were affected by the illness.")

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
