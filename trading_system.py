from data import goods, markets

# Importing necessary classes from caravan_management.py
from caravan_management import Caravan, CaravanResources

# Trading System


class Market:

    def __init__(self, name, goods_prices, currency_exchange_rates):
        self.name = name
        self.goods_prices = goods_prices
        self.currency_exchange_rates = currency_exchange_rates

    def display_goods(self):
        print(f"Goods available in {self.name}:")
        for good, multiplier in self.goods_prices.items():
            price = goods[good]['base_value'] * multiplier
            print(f"{good}: {price} per unit")

    def display_exchange_rates(self):
        print(f"Exchange rates in {self.name}:")
        for currency, rate in self.currency_exchange_rates.items():
            print(f"{currency}: {rate} Gold Coins")


class Player:

    def __init__(self, caravan):
        self.caravan = caravan
        self.goods = {key: 0 for key in goods.keys()}
        self.currencies = self.caravan.resources.__dict__  # Linking player currencies to caravan resources

    def display_inventory(self):
        print("Your goods:")
        for good, quantity in self.goods.items():
            print(f"{good}: {quantity} units")
        print("Your currencies:")
        for currency, amount in self.currencies.items():
            print(f"{currency}: {amount} units")

    def trade_goods(self, market, good, quantity, buying=True):
        if buying:
            cost = goods[good]['base_value'] * market.goods_prices[
                good] * quantity
            if self.currencies['money'] >= cost:
                self.currencies['money'] -= cost
                self.goods[good] += quantity
                print(
                    f"Bought {quantity} units of {good} for {cost} Gold Coins."
                )
            else:
                print("Not enough Gold Coins.")
        else:
            if self.goods[good] >= quantity:
                revenue = goods[good]['base_value'] * market.goods_prices[
                    good] * quantity
                self.currencies['money'] += revenue
                self.goods[good] -= quantity
                print(
                    f"Sold {quantity} units of {good} for {revenue} Gold Coins."
                )
            else:
                print("Not enough goods to sell.")

    def exchange_currency(self, market, from_currency, to_currency, amount):
        from_rate = market.currency_exchange_rates[from_currency]
        to_rate = market.currency_exchange_rates[to_currency]
        if self.currencies[from_currency] >= amount:
            exchanged_amount = amount * to_rate / from_rate
            self.currencies[from_currency] -= amount
            self.currencies[to_currency] += exchanged_amount
            print(
                f"Exchanged {amount} {from_currency} for {exchanged_amount:.2f} {to_currency}."
            )
        else:
            print(f"Not enough {from_currency} to exchange.")


def visit_market(player, market_name):
    market = Market(market_name, markets[market_name], {
        'Gold Coins': 1.0,
        'Dinars': 0.8,
        'Drachms': 1.2
    })
    market.display_goods()
    market.display_exchange_rates()
    player.display_inventory()

    while True:
        action = input("What do you want to do? (buy/sell/exchange/leave): "
                       ).strip().lower()
        if action == "buy":
            good = input("Enter the good you want to buy: ").strip()
            quantity = int(input("Enter the quantity you want to buy: "))
            player.trade_goods(market, good, quantity, buying=True)
        elif action == "sell":
            good = input("Enter the good you want to sell: ").strip()
            quantity = int(input("Enter the quantity you want to sell: "))
            player.trade_goods(market, good, quantity, buying=False)
        elif action == "exchange":
            from_currency = input(
                "Enter the currency you want to exchange from: ").strip()
            to_currency = input(
                "Enter the currency you want to exchange to: ").strip()
            amount = float(
                input(
                    f"Enter the amount of {from_currency} you want to exchange: "
                ))
            player.exchange_currency(market, from_currency, to_currency,
                                     amount)
        elif action == "leave":
            break
        else:
            print("Invalid action. Please try again.")
