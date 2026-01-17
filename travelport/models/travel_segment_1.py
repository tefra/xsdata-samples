from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.segment_1 import Segment1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class TravelSegment1(Segment1):
    """
    Generic segment used to provide travel information that was not
    processed by the system.

    Parameters
    ----------
    origin
        The IATA location code for this origination of this entity.
    destination
        The IATA location code for this destination of this entity.
    departure_time
        The date and time at which this entity departs. This does not
        include time zone information since it can be derived from the
        origin location.
    arrival_time
        The date and time at which this entity arrives at the destination.
        This does not include time zone information since it can be derived
        from the origin location.
    """

    class Meta:
        name = "TravelSegment"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    departure_time: None | str = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
        },
    )
    arrival_time: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        },
    )
