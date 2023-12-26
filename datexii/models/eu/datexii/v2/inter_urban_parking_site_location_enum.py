from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class InterUrbanParkingSiteLocationEnum(Enum):
    """
    Location of the truck or motorway related parking.

    :cvar MOTORWAY: The parking is located directly on a motorway or a
        similar type of road.
    :cvar NEARBY_MOTORWAY: The parking is located with some distance to
        a motorway or a similar type of road but focussed on travellers
        from this motorway.
    :cvar LAY_BY: An area along a road that offers temporary parking.
    :cvar ON_STREET: Vehicles are parking on the roadside.
    :cvar OTHER: The parking is located somewhere else.
    """

    MOTORWAY = "motorway"
    NEARBY_MOTORWAY = "nearbyMotorway"
    LAY_BY = "layBy"
    ON_STREET = "onStreet"
    OTHER = "other"
