from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class DirectionEnum(Enum):
    """
    List of directions of travel.

    :cvar ALL_DIRECTIONS: All directions (where more than two are
        applicable) at this point on the road network.
    :cvar BOTH_WAYS: Both directions that are applicable at this point
        on the road network.
    :cvar CLOCKWISE: Clockwise.
    :cvar ANTICLOCKWISE: Anti-clockwise.
    :cvar INNER_RING: Inner ring direction.
    :cvar OUTER_RING: Outer ring direction.
    :cvar NORTH_BOUND: North bound general direction.
    :cvar NORTH_EAST_BOUND: North east bound general direction.
    :cvar EAST_BOUND: East bound general direction.
    :cvar SOUTH_EAST_BOUND: South east bound general direction.
    :cvar SOUTH_BOUND: South bound general direction.
    :cvar SOUTH_WEST_BOUND: South west bound general direction.
    :cvar WEST_BOUND: West bound general direction.
    :cvar NORTH_WEST_BOUND: North west bound general direction.
    :cvar INBOUND_TOWARDS_TOWN: Heading towards town centre direction of
        travel.
    :cvar OUTBOUND_FROM_TOWN: Heading out of or away from the town
        centre direction of travel.
    :cvar UNKNOWN: Direction is unknown.
    :cvar OPPOSITE: Opposite direction to the normal direction of flow
        at this point on the road network.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    ALL_DIRECTIONS = "allDirections"
    BOTH_WAYS = "bothWays"
    CLOCKWISE = "clockwise"
    ANTICLOCKWISE = "anticlockwise"
    INNER_RING = "innerRing"
    OUTER_RING = "outerRing"
    NORTH_BOUND = "northBound"
    NORTH_EAST_BOUND = "northEastBound"
    EAST_BOUND = "eastBound"
    SOUTH_EAST_BOUND = "southEastBound"
    SOUTH_BOUND = "southBound"
    SOUTH_WEST_BOUND = "southWestBound"
    WEST_BOUND = "westBound"
    NORTH_WEST_BOUND = "northWestBound"
    INBOUND_TOWARDS_TOWN = "inboundTowardsTown"
    OUTBOUND_FROM_TOWN = "outboundFromTown"
    UNKNOWN = "unknown"
    OPPOSITE = "opposite"
    OTHER = "other"
