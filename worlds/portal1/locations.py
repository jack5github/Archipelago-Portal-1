from __future__ import annotations
from BaseClasses import Location
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Portal1World

LOCATION_NAME_TO_ID = {
    "Chamber 00 Flush Toilet": 1,
    "Chamber 00 Detach Security Camera 1": 2,
    "Chamber 00 Detach Security Camera 2": 3,
    "Chamber 00 Radio Dinosaur Noise": 4,
    "Chamber 00 Fizzle Radio": 5,
    "Chamber 00 Detach Security Camera 3": 6,
    "Chamber 01 Detach Security Camera": 7,
    "Chamber 01 Radio Dinosaur Noise": 8,
    "Chamber 01 Fizzle Radio": 9,
    "Chamber 02 Detach Security Camera 1": 10,
    "Chamber 02 Detach Security Camera 2": 11,
    "Chamber 02 Detach Security Camera 3": 12,
    "Chamber 02 Radio Dinosaur Noise": 13,
    "Chamber 02 Fizzle Radio": 14,
    "Chamber 03 Detach Security Camera 1": 15,
    "Chamber 03 Detach Security Camera 2": 16,
    "Chamber 03 Detach Security Camera 3": 17,
    "Chamber 03 Radio Dinosaur Noise": 18,
    "Chamber 03 Fizzle Radio": 19,
    "Chamber 04 Detach Security Camera 1": 20,
    "Chamber 04 Radio Dinosaur Noise": 21,
    "Chamber 04 Fizzle Radio": 22,
    "Chamber 04 Detach Security Camera 2": 23,
    "Chamber 05 Detach Security Camera 1": 24,
    "Chamber 05 Detach Security Camera 2": 25,
    "Chamber 05 Detach Security Camera 3": 26,
    "Chamber 05 Radio Dinosaur Noise": 27,
    "Chamber 05 Fizzle Radio": 28,
    "Chamber 06 Radio Dinosaur Noise": 29,
    "Chamber 06 Fizzle Radio": 30,
    "Chamber 07 Radio Dinosaur Noise": 31,
    "Chamber 07 Fizzle Radio": 32,
    "Chamber 08 Radio Dinosaur Noise": 33,
    "Chamber 08 Fizzle Radio": 34,
    "Chamber 09 Radio Dinosaur Noise": 35,
    "Chamber 09 Fizzle Radio": 36,
    "Chamber 10 Detach Security Camera": 37,
    "Chamber 10 Radio Dinosaur Noise": 38,
    "Chamber 10 Fizzle Radio": 39,
    "Chamber 11 Detach Security Camera": 40,
    "Chamber 11 Radio Dinosaur Noise": 41,
    "Chamber 11 Fizzle Radio": 42,
    "Chamber 12 Radio Dinosaur Noise": 43,
    "Chamber 12 Fizzle Radio": 44,
    "Chamber 13 Detach Security Camera 1": 45,
    "Chamber 13 Detach Security Camera 2": 46,
    "Chamber 13 Radio Dinosaur Noise": 47,
    "Chamber 13 Fizzle Radio": 48,
    "Chamber 13 Detach Security Camera 3": 49,
    "Chamber 13 (Advanced) Detach Security Camera 1": 50,
    "Chamber 13 (Advanced) Detach Security Camera 2": 51,
    "Chamber 13 (Advanced) Detach Security Camera 3": 52,
    "Chamber 14 Radio Dinosaur Noise": 53,
    "Chamber 14 Fizzle Radio": 54,
    "Chamber 15 Detach Security Camera 1": 55,
    "Chamber 15 Radio 1 Dinosaur Noise": 56,
    "Chamber 15 Fizzle Radio 1": 57,
    "Chamber 15 Detach Security Camera 2": 58,
    "Chamber 15 Detach Security Camera 3": 59,
    "Chamber 15 Detach Security Camera 4": 60,
    "Chamber 15 Detach Security Camera 5": 61,
    "Chamber 15 Radio 2 Dinosaur Noise": 62,
    "Chamber 15 Fizzle Radio 2": 63,
    "Chamber 15 (Advanced) Detach Security Camera 1": 64,
    "Chamber 15 (Advanced) Detach Security Camera 2": 65,
    "Chamber 15 (Advanced) Detach Security Camera 3": 66,
    "Chamber 15 (Advanced) Detach Security Camera 4": 67,
    "Chamber 15 (Advanced) Detach Security Camera 5": 68,
    "Chamber 16 Detach Security Camera 1": 69,
    "Chamber 16 Detach Security Camera 2": 70,
    "Chamber 16 Detach Security Camera 3": 71,
    "Chamber 16 Radio Dinosaur Noise": 72,
    "Chamber 16 Fizzle Radio": 73,
    "Chamber 16 Detach Security Camera 4": 74,
    "Chamber 16 Detach Security Camera 5": 75,
    "Chamber 16 (Advanced) Detach Security Camera 1": 76,
    "Chamber 16 (Advanced) Detach Security Camera 2": 77,
    "Chamber 16 (Advanced) Detach Security Camera 3": 78,
    "Chamber 16 (Advanced) Detach Security Camera 4": 79,
    "Chamber 16 (Advanced) Detach Security Camera 5": 80,
    "Chamber 17 Detach Security Camera 1": 81,
    "Chamber 17 Detach Security Camera 2": 82,
    "Chamber 17 Radio Dinosaur Noise": 83,
    "Chamber 17 Fizzle Radio": 84,
    "Chamber 17 (Advanced) Detach Security Camera 1": 85,
    "Chamber 17 (Advanced) Detach Security Camera 2": 86,
    "Chamber 18 Radio Dinosaur Noise": 87,
    "Chamber 18 Fizzle Radio": 88,
    "Chamber 18 Detach Security Camera 1": 89,
    "Chamber 18 Detach Security Camera 2": 90,
    "Chamber 18 (Advanced) Detach Security Camera 1": 91,
    "Chamber 18 (Advanced) Detach Security Camera 2": 92,
    "Chamber 19 Detach Security Camera 1": 93,
    "Chamber 19 Detach Security Camera 2": 94,
    "Chamber 19 Detach Security Camera 3": 95,
}


class Portal1Location(Location):
    game = "Portal"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {
        location_name: LOCATION_NAME_TO_ID[location_name]
        for location_name in location_names
    }


def create_all_locations(world: Portal1World) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: Portal1World) -> None:
    from .options import AdvancedChambers, EscapeSequence

    testchmb_a_00 = world.get_region("Chambers 00-01")
    testchmb_a_01 = world.get_region("Chambers 02-03")
    testchmb_a_02 = world.get_region("Chambers 04-05")
    testchmb_a_03 = world.get_region("Chambers 06-07")
    testchmb_a_04 = world.get_region("Chamber 08")
    testchmb_a_05 = world.get_region("Chamber 09")
    testchmb_a_06 = world.get_region("Chamber 10")
    testchmb_a_07 = world.get_region("Chambers 11-12")
    testchmb_a_08 = world.get_region("Chamber 13")
    testchmb_a_08_advanced = world.get_region("Chamber 13 (Advanced)")
    testchmb_a_09 = world.get_region("Chamber 14")
    testchmb_a_09_advanced = world.get_region("Chamber 14 (Advanced)")
    testchmb_a_10 = world.get_region("Chamber 15")
    testchmb_a_10_advanced = world.get_region("Chamber 15 (Advanced)")
    testchmb_a_11 = world.get_region("Chamber 16")
    testchmb_a_11_advanced = world.get_region("Chamber 16 (Advanced)")
    testchmb_a_13 = world.get_region("Chamber 17")
    testchmb_a_13_advanced = world.get_region("Chamber 17 (Advanced)")
    testchmb_a_14 = world.get_region("Chamber 18")
    testchmb_a_14_advanced = world.get_region("Chamber 18 (Advanced)")
    testchmb_a_15 = world.get_region("Chamber 19 & Escape Part 1")
    escape_00 = world.get_region("Escape Part 2")
    escape_01 = world.get_region("Escape Part 3")
    escape_02 = world.get_region("Escape Part 4 & GLaDOS' Chamber")

    for k in LOCATION_NAME_TO_ID.keys():
        if "Chamber 00" in k or "Chamber 01" in k:
            testchmb_a_00.locations.append(
                Portal1Location(
                    world.player, k, world.location_name_to_id[k], testchmb_a_00
                )
            )
        elif "Chamber 02" in k or "Chamber 03" in k:
            testchmb_a_01.locations.append(
                Portal1Location(
                    world.player, k, world.location_name_to_id[k], testchmb_a_01
                )
            )
        elif "Chamber 04" in k or "Chamber 05" in k:
            testchmb_a_02.locations.append(
                Portal1Location(
                    world.player, k, world.location_name_to_id[k], testchmb_a_02
                )
            )
        elif "Chamber 06" in k or "Chamber 07" in k:
            testchmb_a_03.locations.append(
                Portal1Location(
                    world.player, k, world.location_name_to_id[k], testchmb_a_03
                )
            )
        elif "Chamber 08" in k:
            testchmb_a_04.locations.append(
                Portal1Location(
                    world.player, k, world.location_name_to_id[k], testchmb_a_04
                )
            )
        elif "Chamber 09" in k:
            testchmb_a_05.locations.append(
                Portal1Location(
                    world.player, k, world.location_name_to_id[k], testchmb_a_05
                )
            )
        elif "Chamber 10" in k:
            testchmb_a_06.locations.append(
                Portal1Location(
                    world.player, k, world.location_name_to_id[k], testchmb_a_06
                )
            )
        elif "Chamber 11" in k or "Chamber 12" in k:
            testchmb_a_07.locations.append(
                Portal1Location(
                    world.player, k, world.location_name_to_id[k], testchmb_a_07
                )
            )
        elif "Chamber 13" in k and "Chamber 13 (Advanced)" not in k:
            testchmb_a_08.locations.append(
                Portal1Location(
                    world.player, k, world.location_name_to_id[k], testchmb_a_08
                )
            )
        elif "Chamber 13 (Advanced)" in k:
            if world.options.advanced_chambers != AdvancedChambers.option_normal_only:
                testchmb_a_08_advanced.locations.append(
                    Portal1Location(
                        world.player,
                        k,
                        world.location_name_to_id[k],
                        testchmb_a_08_advanced,
                    )
                )
        elif "Chamber 14" in k and "Chamber 14 (Advanced)" not in k:
            testchmb_a_09.locations.append(
                Portal1Location(
                    world.player, k, world.location_name_to_id[k], testchmb_a_09
                )
            )
        elif "Chamber 14 (Advanced)" in k:
            if world.options.advanced_chambers != AdvancedChambers.option_normal_only:
                testchmb_a_09_advanced.locations.append(
                    Portal1Location(
                        world.player,
                        k,
                        world.location_name_to_id[k],
                        testchmb_a_09_advanced,
                    )
                )
        elif "Chamber 15" in k and "Chamber 15 (Advanced)" not in k:
            testchmb_a_10.locations.append(
                Portal1Location(
                    world.player, k, world.location_name_to_id[k], testchmb_a_10
                )
            )
        elif "Chamber 15 (Advanced)" in k:
            if world.options.advanced_chambers != AdvancedChambers.option_normal_only:
                testchmb_a_10_advanced.locations.append(
                    Portal1Location(
                        world.player,
                        k,
                        world.location_name_to_id[k],
                        testchmb_a_10_advanced,
                    )
                )
        elif "Chamber 16" in k and "Chamber 16 (Advanced)" not in k:
            testchmb_a_11.locations.append(
                Portal1Location(
                    world.player, k, world.location_name_to_id[k], testchmb_a_11
                )
            )
        elif "Chamber 16 (Advanced)" in k:
            if world.options.advanced_chambers != AdvancedChambers.option_normal_only:
                testchmb_a_11_advanced.locations.append(
                    Portal1Location(
                        world.player,
                        k,
                        world.location_name_to_id[k],
                        testchmb_a_11_advanced,
                    )
                )
        elif "Chamber 17" in k and "Chamber 17 (Advanced)" not in k:
            testchmb_a_13.locations.append(
                Portal1Location(
                    world.player, k, world.location_name_to_id[k], testchmb_a_13
                )
            )
        elif "Chamber 17 (Advanced)" in k:
            if world.options.advanced_chambers != AdvancedChambers.option_normal_only:
                testchmb_a_13_advanced.locations.append(
                    Portal1Location(
                        world.player,
                        k,
                        world.location_name_to_id[k],
                        testchmb_a_13_advanced,
                    )
                )
        elif "Chamber 18" in k and "Chamber 18 (Advanced)" not in k:
            testchmb_a_14.locations.append(
                Portal1Location(
                    world.player, k, world.location_name_to_id[k], testchmb_a_14
                )
            )
        elif "Chamber 18 (Advanced)" in k:
            if world.options.advanced_chambers != AdvancedChambers.option_normal_only:
                testchmb_a_14_advanced.locations.append(
                    Portal1Location(
                        world.player,
                        k,
                        world.location_name_to_id[k],
                        testchmb_a_14_advanced,
                    )
                )
        elif "Chamber 19" in k or "Escape Part 1" in k:
            if world.options.escape_sequence != EscapeSequence.option_false:
                testchmb_a_15.locations.append(
                    Portal1Location(
                        world.player, k, world.location_name_to_id[k], testchmb_a_15
                    )
                )
        elif "Escape Part 2" in k:
            if world.options.escape_sequence != EscapeSequence.option_false:
                escape_00.locations.append(
                    Portal1Location(
                        world.player, k, world.location_name_to_id[k], escape_00
                    )
                )
        elif "Escape Part 3" in k:
            if world.options.escape_sequence != EscapeSequence.option_false:
                escape_01.locations.append(
                    Portal1Location(
                        world.player, k, world.location_name_to_id[k], escape_01
                    )
                )
        elif "Escape Part 4" in k or "GLaDOS' Chamber" in k:
            if world.options.escape_sequence != EscapeSequence.option_false:
                escape_02.locations.append(
                    Portal1Location(
                        world.player, k, world.location_name_to_id[k], escape_02
                    )
                )
        else:
            raise RuntimeError(f"Location name {k!r} has indeterminate region")


def create_events(world: Portal1World) -> None:
    """
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    top_left_room = world.get_region("Top Left Room")
    final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    button_in_top_left_room = Portal1Location(
        world.player, "Top Left Room Button", None, top_left_room
    )
    top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    button_item = items.Portal1Item(
        "Top Left Room Button Pressed",
        ItemClassification.progression,
        None,
        world.player,
    )
    button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    final_boss_room.add_event(
        "Final Boss Defeated",
        "Victory",
        location_type=Portal1Location,
        item_type=items.Portal1Item,
    )

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
    """
