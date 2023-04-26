import app
from flask import Flask
from dataclasses import dataclass


@dataclass
class Item:
    iid: int
    name: str
    value: float
    quantity: int
    description: str = None


def item_list():
    return [
        Item(1, "Potion", 5.00, 10, "Heals you for 10 hp"),
        Item(2, "Super Potion", 10.00, 5, "Heals you for 20 hp"),
        Item(3, "Hyper Potion", 15.00, 2, "Heals you for 50 hp"),
        Item(4, "Max Potion", 20.00, 1, "Heals you for all hp"),
        Item(5, "Pokeball", 2.00, 20, "Catch a pokemon"),
        Item(6, "Greatball", 5.00, 10, "Catch a pokemon"),
        Item(7, "Ultraball", 10.00, 5, "Catch a pokemon"),
        Item(8, "Masterball", 50.00, 1, "Catch a pokemon"),
        Item(9, "Revive", 10.00, 5, "Revive a fainted pokemon"),
        Item(10, "Max Revive", 20.00, 2, "Revive a fainted pokemon"),
        Item(11, "Razz Berry", 0.50, 20, "Increase chance of catching a pokemon"),
        Item(12, "Nanab Berry", 0.50, 20, "Decrease chance of being caught by a pokemon"),
        Item(13, "Pinap Berry", 0.50, 20, "Increase amount of candy received when catching a pokemon"),
        Item(14, "Sun Stone", 20.00, 1, "Evolve certain pokemon"),
        Item(15, "Kings Rock", 20.00, 1, "Evolve certain pokemon"),
        Item(16, "Metal Coat", 20.00, 1, "Evolve certain pokemon"),
        Item(17, "Dragon Scale", 20.00, 1, "Evolve certain pokemon"),
        Item(18, "Up-grade", 20.00, 1, "Evolve certain pokemon")
    ]

# This is a lambda function that returns a list of items that match the given criteria

def get_item(criteria: lambda item: item.name == item.name):
    return [item for item in item_list() if criteria(item)]

def get_card(item):
    return f"""
    {item.name} - ${item.value}
    {item.description}
    """

