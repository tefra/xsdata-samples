from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingTypeOfGroup(Enum):
    """
    The type of group specification (group of parking spaces).

    :cvar ADJACENT_SPACES: A description of adjacent spaces.
    :cvar NON_ADJACENT_SPACES: A description of non-adjacent spaces.
    :cvar COMPLETE_FLOOR: A description for a complete floor in a car
        park.
    :cvar MIXED_USAGE: A definition for mixed usage for this group (e.g.
        by time). This means there are more definitions for this group
        or for sub- or supersets of it.
    :cvar STATISTICS_ONLY: This group provides statistical figures only,
        for example 60 spaces for lorries in total. Usually, this kind
        of group does not use georeference information.  It is not a
        complete description of parking spaces.
    :cvar SINGLE_PARAMETERS: This group provides some single features
        for a selected number of spaces. For example, you can define all
        spaces, where electric charging stations are provided. It is not
        a complete description of the parking spaces.
    :cvar OTHER: Some other kind of group.
    """
    ADJACENT_SPACES = "adjacentSpaces"
    NON_ADJACENT_SPACES = "nonAdjacentSpaces"
    COMPLETE_FLOOR = "completeFloor"
    MIXED_USAGE = "mixedUsage"
    STATISTICS_ONLY = "statisticsOnly"
    SINGLE_PARAMETERS = "singleParameters"
    OTHER = "other"
