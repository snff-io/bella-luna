from dataclasses import dataclass
from flask import Flask, render_template

app = Flask(__name__)

@dataclass
class item:
    gid: int
    name: str
    value: float
    quantity: int
    description: str = None


def item_list():
    return {
    1: item(1, "Potion", 5.00, 10, "Heals you for 10 hp"),
    2: item(2, "Super Potion", 10.00, 5, "Heals you for 20 hp"),
    3: item(3, "Hyper Potion", 15.00, 2, "Heals you for 50 hp"),
    4: item(4, "Max Potion", 20.00, 1, "Heals you for all hp"),
    5: item(5, "Pokeball", 2.00, 20, "Catch a pokemon"),
    6: item(6, "Greatball", 5.00, 10, "Catch a pokemon"),
    7: item(7, "Ultraball", 10.00, 5, "Catch a pokemon"),
    8: item(8, "Masterball", 50.00, 1, "Catch a pokemon"),
    9: item(9, "Revive", 10.00, 5, "Revive a fainted pokemon"),
    10: item(10, "Max Revive", 20.00, 2, "Revive a fainted pokemon"),
    11: item(11, "Razz Berry", 0.50, 20, "Increase chance of catching a pokemon"),
    12: item(12, "Nanab Berry", 0.50, 20, "Decrease chance of being caught by a pokemon"),
    13: item(13, "Pinap Berry", 0.50, 20, "Increase amount of candy received when catching a pokemon"),
    14: item(14, "Sun Stone", 20.00, 1, "Evolve certain pokemon"),
    15: item(15, "Kings Rock", 20.00, 1, "Evolve certain pokemon"),
    16: item(16, "Metal Coat", 20.00, 1, "Evolve certain pokemon"),
    17: item(17, "Dragon Scale", 20.00, 1, "Evolve certain pokemon"),
    18: item(18, "Up-grade", 20.00, 1, "Evolve certain pokemon")
}

# This is a lambda function that returns a list of items that match the given criteria
def get_item(criteria: lambda name : name.endsWith("Potion")):
    item_list().values(criteria)  