from dataclasses import dataclass
from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class StartingMap(Choice):
    """
    The map to start on.
    """

    display_name = "Starting Map"

    option_chamber_00 = 0
    option_random_chamber = 1
    option_random_map = 2

    default = option_random_chamber


class AdvancedChambers(Choice):
    """
    How to include advanced chambers in the pool.
    """

    display_name = "Advanced Chambers"

    option_normal_only = 0
    option_advanced_replaces_normal = 1
    option_normal_and_advanced = 2

    default = option_normal_only


class AdvancedChamberCount(Range):
    """
    The number of advanced chambers to randomly include. Only applies if 'Advanced Chambers' is not 'Normal Only'.
    """

    display_name = "Advanced Chamber Count"

    range_start = 0
    range_end = 6

    default = 3


class EscapeSequence(Toggle):
    """
    Whether to include the Escape Sequence and GLaDOS' Chamber in the pool.
    """

    display_name = "Escape Sequence"

    default = 1


class Radios(Toggle):
    """
    Whether to make radios initially invisible and require them to be unlocked.
    """

    display_name = "Radios"

    default = 0


class DinosaurHunt(Choice):
    """
    Whether to consider taking radios to their "dinosaur" noise locations as checks.

    - Disabled - Dinosaur checks are not included.
    - Normal - Dinosaur checks are included. Noise locations are the same as normal.
    - Random Positions - Dinosaur checks are included. Noise locations are randomly moved.
    """

    display_name = "Dinosaur Hunt"

    option_disabled = 0
    option_normal = 1
    option_random_positions = 2

    default = 0


class TrapChance(Range):
    """
    Percentage chance that a filler item will be a trap.
    """

    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 10


@dataclass
class Portal1Options(PerGameCommonOptions):
    starting_map: StartingMap
    advanced_chambers: AdvancedChambers
    advanced_chamber_count: AdvancedChamberCount
    escape_sequence: EscapeSequence
    radios: Radios
    dinosaur_hunt: DinosaurHunt
    trap_chance: TrapChance


option_groups = [
    OptionGroup(
        "Map Options",
        [StartingMap, AdvancedChambers, AdvancedChamberCount, EscapeSequence],
    ),
    OptionGroup("Gameplay Options", [Radios, DinosaurHunt, TrapChance]),
]

option_presets = {
    # Like the Advanced Chambers, emphasise slow-going playthroughs with a higher trap chance
    "Advanced Preset": {
        "starting_map": StartingMap.option_random_map,
        "advanced_chambers": AdvancedChambers.option_normal_and_advanced,
        "advanced_chamber_count": AdvancedChamberCount.range_end,
        "escape_sequence": EscapeSequence.option_true,
        "radios": Radios.option_true,
        "dinosaur_hunt": DinosaurHunt.option_random_positions,
        "trap_chance": TrapChance.default * 2,
    },
    # Like the Challenges, emphasise fast-going playthroughs with the highest trap chance (but not any traps that slow things down)
    "Challenge Preset": {
        "starting_map": StartingMap.option_random_map,
        "advanced_chambers": AdvancedChambers.option_advanced_replaces_normal,
        "advanced_chamber_count": AdvancedChamberCount.range_end,
        "escape_sequence": EscapeSequence.option_false,
        "radios": Radios.option_false,
        "dinosaur_hunt": DinosaurHunt.option_disabled,
        "trap_chance": TrapChance.range_end,
    },
}
