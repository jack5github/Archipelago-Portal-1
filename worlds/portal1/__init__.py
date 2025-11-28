from BaseClasses import Tutorial
from collections.abc import Mapping
from typing import Any
from worlds.AutoWorld import WebWorld, World
from . import items, locations, options, regions, rules


class Portal1WebWorld(WebWorld):
    game = "Portal"

    theme = "ice"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Portal 1 for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Jack5"],
    )

    tutorials = [setup_en]

    option_groups = options.option_groups
    options_presets = options.option_presets


class Portal1World(World):
    """
    Portal is a single player game from Valve. Set in the mysterious Aperture Science Laboratories, Portal has been called one of the most innovative new games on the horizon and will offer gamers hours of unique gameplay.
    The game is designed to change the way players approach, manipulate, and surmise the possibilities in a given environment; similar to how Half-Life 2's Gravity Gun innovated new ways to leverage an object in any given situation.
    Players must solve physical puzzles and challenges by opening portals to maneuvering objects, and themselves, through space.
    """

    game = "Portal"

    web = Portal1WebWorld()

    options_dataclass = options.Portal1Options
    options: options.Portal1Options

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.Portal1Item:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(*self.options_dataclass.__dataclass_fields__.keys())
