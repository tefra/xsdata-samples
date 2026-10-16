from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


class OptionalServiceApplicabilityType4(StrEnum):
    """
    The different levels at which an optional service may be applied.

    Properties
    ----------
    ITINERARY
    PASSENGER
    SEGMENT
    PASSENGER_SEGMENT
    PASSENGER_OD
        PassengerOD stands for passenger origin destination.
    OTHER
    """

    ITINERARY = "Itinerary"
    PASSENGER = "Passenger"
    SEGMENT = "Segment"
    PASSENGER_SEGMENT = "PassengerSegment"
    PASSENGER_OD = "PassengerOD"
    OTHER = "Other"
