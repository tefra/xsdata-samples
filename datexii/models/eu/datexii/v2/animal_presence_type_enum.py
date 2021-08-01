from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class AnimalPresenceTypeEnum(Enum):
    """
    Types of animal presence.

    :cvar ANIMALS_ON_THE_ROAD: Traffic may be disrupted due to animals
        on the roadway.
    :cvar HERD_OF_ANIMALS_ON_THE_ROAD: Traffic may be disrupted due to a
        herd of animals on the roadway.
    :cvar LARGE_ANIMALS_ON_THE_ROAD: Traffic may be disrupted due to
        large animals on the roadway.
    """
    ANIMALS_ON_THE_ROAD = "animalsOnTheRoad"
    HERD_OF_ANIMALS_ON_THE_ROAD = "herdOfAnimalsOnTheRoad"
    LARGE_ANIMALS_ON_THE_ROAD = "largeAnimalsOnTheRoad"
