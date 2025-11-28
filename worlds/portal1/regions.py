from __future__ import annotations
from BaseClasses import Region
from typing import TYPE_CHECKING
from .options import AdvancedChambers

if TYPE_CHECKING:
    from . import Portal1World

region_strings: list[str] = [
    "Menu",
    "Chambers 00-01",
    "Chambers 02-03",
    "Chambers 04-05",
    "Chambers 06-07",
    "Chamber 08",
    "Chamber 09",
    "Chamber 10",
    "Chambers 11-12",
    "Chamber 13",
    "Chamber 13 (Advanced)",
    "Chamber 14",
    "Chamber 14 (Advanced)",
    "Chamber 15",
    "Chamber 15 (Advanced)",
    "Chamber 16",
    "Chamber 16 (Advanced)",
    "Chamber 17",
    "Chamber 17 (Advanced)",
    "Chamber 18",
    "Chamber 18 (Advanced)",
    "Chamber 19 & Escape Part 1",
    "Escape Part 2",
    "Escape Part 3",
    "Escape Part 4 & GLaDOS' Chamber",
]


def create_and_connect_regions(world: Portal1World) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: Portal1World) -> None:
    regions = [Region(k, world.player, world.multiworld) for k in region_strings]
    # TODO: Fix not including regions creating KeyErrors when adding locations
    """if "(Advanced)" not in k"""

    """if world.options.advanced_chambers in [
        AdvancedChambers.option_advanced_replaces_normal,
        AdvancedChambers.option_normal_and_advanced,
    ]:
        regions.extend(
            [
                Region(k, world.player, world.multiworld)
                for k in region_strings
                if "(Advanced)" in k
            ]
        )"""

    world.multiworld.regions += regions


def connect_regions(world: Portal1World) -> None:
    from BaseClasses import Entrance

    menu = world.get_region("Menu")

    for region in region_strings:
        if region == "Menu" or (
            "(Advanced)" in region
            and world.options.advanced_chambers == AdvancedChambers.option_normal_only
        ):
            continue
        region = world.get_region(region)
        menu.connect(region, f"{menu.name} to {region.name}")
