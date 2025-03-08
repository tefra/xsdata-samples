from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.book_flight_segment_type import BookFlightSegmentType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class OriginDestinationOptionType:
    """
    A container for flight segments.

    Attributes:
        flight_segment: A container for necessary data to describe one
            or more legs of a single flight number.
        elapsed_time: Elapsed leg trip time in minutes
    """

    flight_segment: list[BookFlightSegmentType] = field(
        default_factory=list,
        metadata={
            "name": "FlightSegment",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
            "max_occurs": 4,
        },
    )
    elapsed_time: None | int = field(
        default=None,
        metadata={
            "name": "ElapsedTime",
            "type": "Attribute",
        },
    )
