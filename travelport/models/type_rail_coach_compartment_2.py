from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeRailCoachCompartment2(Enum):
    """
    The type of Rail Caoch Compartment.
    """
    SEAT_COUCHETTE = "Seat/Couchette"
    QUIET = "Quiet"
    OFFICE = "Office"
    TABLE = "Table"
    WHEELCHAIR_PLACE = "Wheelchair Place"
    AIR_CONDITIONED = "Air-conditioned"
    LOUNGE = "Lounge"
    RECLINING = "Reclining"
