from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingModeEnum(Enum):
    """
    The arrangement of the parking space or the group of parking spaces in relation
    to the road.

    :cvar PERPENDICULAR_PARKING: Parking spaces are located in an angle
        of nearly 90 degree to the road.
    :cvar PARALLEL_PARKING: Parking spaces are located parallel to the
        road.
    :cvar ECHELON_PARKING: Parking spaces are located in a diagonal
        relation to the road.
    :cvar PARKING_ON_OPPOSITE_SIDE_OF_ROAD: Parking is possible on the
        other side of the road.
    :cvar OTHER: Other.
    """

    PERPENDICULAR_PARKING = "perpendicularParking"
    PARALLEL_PARKING = "parallelParking"
    ECHELON_PARKING = "echelonParking"
    PARKING_ON_OPPOSITE_SIDE_OF_ROAD = "parkingOnOppositeSideOfRoad"
    OTHER = "other"
