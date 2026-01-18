from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class CarriagewayEnum(Enum):
    """
    List of descriptors identifying specific carriageway details.

    :cvar CONNECTING_CARRIAGEWAY: On the connecting carriageway.
    :cvar ENTRY_SLIP_ROAD: On the entry slip road.
    :cvar EXIT_SLIP_ROAD: On the exit slip road.
    :cvar FLYOVER: On the flyover, i.e. the section of road passing over
        another.
    :cvar LEFT_HAND_FEEDER_ROAD: On the left hand feeder road.
    :cvar LEFT_HAND_PARALLEL_CARRIAGEWAY: On the left hand parallel
        carriageway.
    :cvar MAIN_CARRIAGEWAY: On the main carriageway.
    :cvar OPPOSITE_CARRIAGEWAY: On the opposite carriageway.
    :cvar PARALLEL_CARRIAGEWAY: On the adjacent parallel carriageway.
    :cvar RIGHT_HAND_FEEDER_ROAD: On the right hand feeder road.
    :cvar RIGHT_HAND_PARALLEL_CARRIAGEWAY: On the right hand parallel
        carriageway.
    :cvar ROUNDABOUT: On the roundabout.
    :cvar SERVICE_ROAD: On the adjacent service road.
    :cvar SLIP_ROADS: On the slip roads.
    :cvar UNDERPASS: On the underpass, i.e. the section of road passing
        under another.
    """

    CONNECTING_CARRIAGEWAY = "connectingCarriageway"
    ENTRY_SLIP_ROAD = "entrySlipRoad"
    EXIT_SLIP_ROAD = "exitSlipRoad"
    FLYOVER = "flyover"
    LEFT_HAND_FEEDER_ROAD = "leftHandFeederRoad"
    LEFT_HAND_PARALLEL_CARRIAGEWAY = "leftHandParallelCarriageway"
    MAIN_CARRIAGEWAY = "mainCarriageway"
    OPPOSITE_CARRIAGEWAY = "oppositeCarriageway"
    PARALLEL_CARRIAGEWAY = "parallelCarriageway"
    RIGHT_HAND_FEEDER_ROAD = "rightHandFeederRoad"
    RIGHT_HAND_PARALLEL_CARRIAGEWAY = "rightHandParallelCarriageway"
    ROUNDABOUT = "roundabout"
    SERVICE_ROAD = "serviceRoad"
    SLIP_ROADS = "slipRoads"
    UNDERPASS = "underpass"
