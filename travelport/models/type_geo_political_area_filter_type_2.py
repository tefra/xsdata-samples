from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeGeoPoliticalAreaFilterType2(Enum):
    """
    Properties
    ----------
    ARRIVAL
        Filter type applied on Air and Rail Preference
    DEPARTURE
        Filter type applied on Air,Hotel,Rail and Vehicle Preference
    CONNECTION
        Filter type applied on Air and Rail Preference
    OTHER
        Filter type applied on Advisory and Other Preference
    """
    ARRIVAL = "Arrival"
    DEPARTURE = "Departure"
    CONNECTION = "Connection"
    OTHER = "Other"
