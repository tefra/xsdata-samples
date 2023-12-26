from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class ModificationType1(Enum):
    """
    The modification types supported.

    Properties
    ----------
    ADD_SEGMENT
        Add a segment to the itinerary
    REMOVE_SEGMENT
        Delete a segment from the itinerary
    REPLACE_SEGMENT
        Replace a segment in the itinerary with a new segment
    ADD_PASSENGER
        Add a passenger to the itinerary
    REMOVE_PASSENGER
        Remove a passenger from the itinerary
    OPTIONS_ONLY
        Modification where only options are added / removed from the
        itinerary
    OTHER
        Other modification types
    """

    ADD_SEGMENT = "AddSegment"
    REMOVE_SEGMENT = "RemoveSegment"
    REPLACE_SEGMENT = "ReplaceSegment"
    ADD_PASSENGER = "AddPassenger"
    REMOVE_PASSENGER = "RemovePassenger"
    OPTIONS_ONLY = "OptionsOnly"
    OTHER = "Other"
