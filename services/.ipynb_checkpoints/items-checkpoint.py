from dataclasses import dataclass

@dataclass
class item:
    iid: int
    name: str
    value: float
    quantity: int
    description: str = None


def item_list():
    return [
        item(1, "Potion", 5.00, 10, "Heals you for 10 hp"),
        item(2, "Super Potion", 10.00, 5, "Heals you for 20 hp"),
        item(3, "Hyper Potion", 15.00, 2, "Heals you for 50 hp"),
        item(4, "Max Potion", 20.00, 1, "Heals you for all hp"),
        item(5, "Pokeball", 2.00, 20, "Catch a pokemon"),
        item(6, "Greatball", 5.00, 10, "Catch a pokemon"),
        item(7, "Ultraball", 10.00, 5, "Catch a pokemon"),
        item(8, "Masterball", 50.00, 1, "Catch a pokemon"),
        item(9, "Revive", 10.00, 5, "Revive a fainted pokemon"),
        item(10, "Max Revive", 20.00, 2, "Revive a fainted pokemon"),
        item(11, "Razz Berry", 0.50, 20, "Increase chance of catching a pokemon"),
        item(12, "Nanab Berry", 0.50, 20, "Decrease chance of being caught by a pokemon"),
        item(13, "Pinap Berry", 0.50, 20, "Increase amount of candy received when catching a pokemon"),
        item(14, "Sun Stone", 20.00, 1, "Evolve certain pokemon"),
        item(15, "Kings Rock", 20.00, 1, "Evolve certain pokemon"),
        item(16, "Metal Coat", 20.00, 1, "Evolve certain pokemon"),
        item(17, "Dragon Scale", 20.00, 1, "Evolve certain pokemon"),
        item(18, "Up-grade", 20.00, 1, "Evolve certain pokemon")
    ]


# This is a lambda function that returns a list of items that match the given criteria


def get_item(criteria: lambda name: name.endsWith("Potion")):
    return [item for item in item_list() if criteria(itemddddddddddddddddddddddddddddddddddd)]
