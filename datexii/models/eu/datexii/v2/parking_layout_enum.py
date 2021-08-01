from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingLayoutEnum(Enum):
    """
    Types of layout of the parking site.

    :cvar MULTI_STOREY: Parking is on multiple levels within a parking
        building.
    :cvar SINGLE_LEVEL: Parking is inside a building on a single ground
        floor level.
    :cvar UNDERGROUND: Parking is on one or more floors below ground
        level.
    :cvar UNDERGROUND_AND_MULTISTOREY: Parking is on multiple floors
        levels including both below and above ground level.
    :cvar AUTOMATED_PARKING_GARAGE: Parking is completely automated from
        the point of leaving the vehicle in an arrival bay to its
        delivery back to the driver in a pickup bay.
    :cvar OPEN_SPACE: A normal ground level parking place.
    :cvar COVERED: Some covered parking space.
    :cvar NESTED: A parking space within a complex structure of
        buildings or surrounded by buildings.
    :cvar FIELD: A non-bituminized parking space (e.g. for events or as
        extension).
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """
    MULTI_STOREY = "multiStorey"
    SINGLE_LEVEL = "singleLevel"
    UNDERGROUND = "underground"
    UNDERGROUND_AND_MULTISTOREY = "undergroundAndMultistorey"
    AUTOMATED_PARKING_GARAGE = "automatedParkingGarage"
    OPEN_SPACE = "openSpace"
    COVERED = "covered"
    NESTED = "nested"
    FIELD = "field"
    UNKNOWN = "unknown"
    OTHER = "other"
