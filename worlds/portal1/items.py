from __future__ import annotations
from BaseClasses import Item, ItemClassification
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Portal1World

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Progressive Portal Gun (1 Portal)": (
        ItemClassification.progression | ItemClassification.useful
    ),
    "Progressive Portal Gun (2 Portals)": (
        ItemClassification.progression | ItemClassification.useful
    ),
    "Long Fall Boots": ItemClassification.progression | ItemClassification.useful,
    "HEV Suit (Faster Walk Speed)": ItemClassification.useful,
    "Progressive Dinosaur Radar (1: Find Radios)": ItemClassification.useful,
    "Progressive Dinosaur Radar (2: Find Noises)": ItemClassification.useful,
    "Speedup": ItemClassification.filler,
    "Slowdown": ItemClassification.trap,
    "Chambers 00-01 Unlock": ItemClassification.progression,
}
# TODO: Restore these items once there are more locations than items
"""
    "Blindness": ItemClassification.trap,
    "Stuck": ItemClassification.trap,
    "Low Gravity": ItemClassification.filler,
    "High Gravity": ItemClassification.trap,
    "Portals Never Fail": ItemClassification.filler,
    "No Portal Gun": ItemClassification.trap,
    "Mid-air Portal": ItemClassification.trap,
    "Weighted Storage Cube": ItemClassification.filler,
    "Weighted Storage Sphere": ItemClassification.filler,
    "Barrel": ItemClassification.filler,
    "Explosive Barrel": ItemClassification.trap,
    "Random Prop": ItemClassification.trap,
    "Half-Life 2 Revolver": ItemClassification.filler,
    "Half-Life 2 Grenade": ItemClassification.filler,
    "Half-Life 2 Rocket": ItemClassification.filler,
    "Airboat": ItemClassification.filler,
    "Instant Energy Pellet": ItemClassification.trap,
    "Turret": ItemClassification.trap,
    "Rocket Turret": ItemClassification.trap,
    # TODO: Move "Chambers 00-01 Unlock" here
    "Chambers 02-03 Unlock": ItemClassification.progression,
    "Chambers 04-05 Unlock": ItemClassification.progression,
    "Chambers 06-07 Unlock": ItemClassification.progression,
    "Chamber 08 Unlock": ItemClassification.progression,
    "Chamber 09 Unlock": ItemClassification.progression,
    "Chamber 10 Unlock": ItemClassification.progression,
    "Chambers 11-12 Unlock": ItemClassification.progression,
    "Chamber 13 Unlock": ItemClassification.progression,
    "Chamber 13 (Advanced) Unlock": ItemClassification.progression,
    "Chamber 14 Unlock": ItemClassification.progression,
    "Chamber 14 (Advanced) Unlock": ItemClassification.progression,
    "Chamber 15 Unlock": ItemClassification.progression,
    "Chamber 15 (Advanced) Unlock": ItemClassification.progression,
    "Chamber 16 Unlock": ItemClassification.progression,
    "Chamber 16 (Advanced) Unlock": ItemClassification.progression,
    "Chamber 17 Unlock": ItemClassification.progression,
    "Chamber 17 (Advanced) Unlock": ItemClassification.progression,
    "Chamber 18 Unlock": ItemClassification.progression,
    "Chamber 18 (Advanced) Unlock": ItemClassification.progression,
    "Chamber 19 & Escape Part 1 Unlock": ItemClassification.progression,
    "Escape Part 2 Unlock": ItemClassification.progression,
    "Escape Part 3 Unlock": ItemClassification.progression,
    "Escape Part 4 & GLaDOS' Chamber Unlock": ItemClassification.progression,
    "Defeat GLaDOS": ItemClassification.progression,
"""

ITEM_NAME_TO_ID = {k: i + 1 for i, k in enumerate(DEFAULT_ITEM_CLASSIFICATIONS.keys())}


class Portal1Item(Item):
    game = "Portal"


def is_progression(item_class: ItemClassification) -> bool:
    return bool(item_class & ItemClassification.progression)


def is_useful(item_class: ItemClassification) -> bool:
    return bool(item_class & ItemClassification.useful)


def is_filler(item_class: ItemClassification) -> bool:
    # Filler is 0b00000, therefore equality check is needed
    return item_class == ItemClassification.filler


def is_trap(item_class: ItemClassification) -> bool:
    return bool(item_class & ItemClassification.trap)


def get_random_filler_item_name(world: Portal1World) -> str:
    if world.random.randint(0, 99) < world.options.trap_chance:
        return world.random.choice(
            [k for k, v in DEFAULT_ITEM_CLASSIFICATIONS.items() if is_trap(v)]
        )
    return world.random.choice(
        [k for k, v in DEFAULT_ITEM_CLASSIFICATIONS.items() if is_filler(v)]
    )


def create_item_with_correct_classification(
    world: Portal1World, name: str
) -> Portal1Item:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    if "Progressive Dinosaur Radar" in name and world.options.dinosaur_hunt:
        classification = ItemClassification.progression | ItemClassification.useful

    return Portal1Item(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: Portal1World) -> None:
    from .options import StartingMap

    itempool: list[Item] = [
        world.create_item(k)
        for k, v in DEFAULT_ITEM_CLASSIFICATIONS.items()
        if not is_filler(v) and not is_trap(v)
    ]

    """
    # Some items may only exist if the player enables certain options.
    # In our case, If the hammer option is enabled, the sixth item is the Hammer.
    # Otherwise, we add a filler Confetti Cannon.
    if world.options.hammer:
        # Once again, it is important to stress that even though the Hammer doesn't always exist,
        # it must be present in the worlds item_name_to_id.
        # Whether it is actually in the itempool is determined purely by whether we create and add the item here.
        itempool.append(world.create_item("Hammer"))
    """

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(
        world.multiworld.get_unfilled_locations(world.player)
    )

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

    if world.options.starting_map == StartingMap.option_chamber_00:
        world.push_precollected(world.create_item("Chambers 00-01 Unlock"))
    else:
        choices: list[str] = [
            k for k in DEFAULT_ITEM_CLASSIFICATIONS.keys() if "Unlock" in k
        ]
        if world.options.starting_map == StartingMap.option_random_chamber:
            choices = [k for k in choices if k.startswith("Chamber")]
        world.push_precollected(world.create_item(world.random.choice(choices)))


if __name__ == "__main__":
    for k, v in DEFAULT_ITEM_CLASSIFICATIONS.items():
        item_string: str = f"{k}: ("
        if is_progression(v):
            item_string += "Progression, "
        if is_useful(v):
            item_string += "Useful, "
        if is_filler(v):
            item_string += "Filler, "
        if is_trap(v):
            item_string += "Trap, "
        item_string = f"{item_string[:-2]})"
        print(item_string)
