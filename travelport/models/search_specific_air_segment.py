from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SearchSpecificAirSegment:
    """
    Parameters
    ----------
    departure_time
        The date and time at which this entity departs. This does not
        include time zone information since it can be derived from the
        origin location.
    carrier
        The carrier that is marketing this segment
    flight_number
        The flight number under which the marketing carrier is marketing
        this flight
    origin
        The IATA location code for this origination of this entity.
    destination
        The IATA location code for this destination of this entity.
    segment_index
        The sequential AirSegment number that this segment connected to.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    departure_time: None | str = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
            "required": True,
        },
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        },
    )
    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        },
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
    segment_index: None | int = field(
        default=None,
        metadata={
            "name": "SegmentIndex",
            "type": "Attribute",
        },
    )
