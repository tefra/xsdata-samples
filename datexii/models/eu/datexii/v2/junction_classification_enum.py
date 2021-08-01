from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class JunctionClassificationEnum(Enum):
    """
    Explicit type of a junction.

    :cvar THREE_WAY_INTERCHANGE: One motorway merging into another (with
        three legs in total).
    :cvar INTERCHANGE: Usually two crossing motorways (four legs, but
        can be even more).
    :cvar MOTORWAY_CONNECTION: Beginning or end of a motorway (e.g.
        changeover to smaller road).
    :cvar JUNCTION: Entrance and exit on a motorway.
    :cvar TEMPORARY_JUNCTION: Entrance and exit on a motorway, reserved
        either for emergency and service or on a temporary basis.
    :cvar BORDER_CROSSING: Motorway crossing a border (between counties,
        countries, states, ...).
    :cvar JUNCTION_IN_ONE_DIRECTION: Entry and Exit on a motorway, where
        just one direction of the motorway is accessible.
    :cvar OPERATIONAL_SERVICE_JUNCTION: Junction accessible only for
        operational services.
    :cvar OTHER: Other.
    """
    THREE_WAY_INTERCHANGE = "threeWayInterchange"
    INTERCHANGE = "interchange"
    MOTORWAY_CONNECTION = "motorwayConnection"
    JUNCTION = "junction"
    TEMPORARY_JUNCTION = "temporaryJunction"
    BORDER_CROSSING = "borderCrossing"
    JUNCTION_IN_ONE_DIRECTION = "junctionInOneDirection"
    OPERATIONAL_SERVICE_JUNCTION = "operationalServiceJunction"
    OTHER = "other"
