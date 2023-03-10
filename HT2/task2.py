# There is a Person whose characteristics are:
# 1. Name
# 2. Age
# 3. Availability of money
# 4. Having your own home
#
# Human can:
# 1. Provide information about yourself
# 2. Make money
# 3. Buy a house
# There is also a House, the properties of which include:
# 1. Area
# 2. Cost
#
# For Home you can:
# 1. Apply a purchase discount
# e.g.: There is also a Small Typical House with a required area of
# 40m2.
#
# *Realtor:
# 1. Name
# 2. Houses
# 3. Discount that he/she can give you.
# *There is only one realtor who handles small houses you wanna
# buy. (Singleton)
# Realtor is only one in your city and can:
# 1. Provide information about all the Houses
# 2. Give a discount
# 3. Steal your money with 10% chance

import random


class Buyer:
    def __init__(self, name, age, money, house):
        self.name = name
        self.age = age
        self.money = money
        self.house = house

    def provide_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Money:", self.money)
        print("Home:", self.house)

    def make_money(self, amount):
        self.money += amount

    def buy_home(self, home):
        if self.money >= home.cost:
            self.money -= home.cost
            self.house = True
            print(f"{self.name} has bought a home with area {home.area}m2 for {home.cost}ua!")
        else:
            print(f"{self.name} does not have enough money.")


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def apply_discount(self, discount):
        self.cost *= (1 - discount)
        print(f"You have discount! New cost: {self.cost}$")


class Realtor:
    good_realtor = None

    def __new__(cls, name, houses, discount):
        if cls.good_realtor is None:
            cls.good_realtor = super().__new__(cls)
            cls.good_realtor.name = name
            cls.good_realtor.houses = houses
            cls.good_realtor.discount = discount
        return cls.good_realtor

    def provide_info(self):
        print(f"Realtor Name: {self.name}")
        for i, house in enumerate(self.houses):
            print(f"House {i + 1}: area {house.area}m2, cost {house.cost}ua")

    def have_discount(self, house):
        house.apply_discount(self.discount)

    def steal_money(self, person):
        if random.random() < 0.1:
            stolen_amount = person.money // 2  # steal half of person's money
            person.money -= stolen_amount
            print(f"Sorry! {self.name} has stolen {stolen_amount}ua from {person.name}!")
        else:
            print(f"Good. {self.name} did not steal any money.")


# Example usage
small_house = House(40, 500000)
buyer = Buyer("Slava", 27, 700000, False)
realtor = Realtor("Igor", [small_house], 0.1)

buyer.provide_info()
buyer.make_money(10000)
buyer.provide_info()

realtor.provide_info()
realtor.have_discount(small_house)
realtor.steal_money(buyer)

buyer.buy_home(small_house)
buyer.provide_info()
