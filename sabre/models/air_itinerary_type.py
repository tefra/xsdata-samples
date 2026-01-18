from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from sabre.models.air_trip_type import AirTripType
from sabre.models.origin_destination_option_type import (
    OriginDestinationOptionType,
)

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class AirItineraryType:
    """
    Specifies the origin and destination of the traveler.

    Attributes:
        origin_destination_options: A collection of
            OriginDestinationOption
        direction_ind: A directional indicator that identifies a type of
            air booking (e.g. one-way, round-trip, open-jaw).
        departure_date: Itinerary departure date
    """

    origin_destination_options: (
        None | AirItineraryType.OriginDestinationOptions
    ) = field(
        default=None,
        metadata={
            "name": "OriginDestinationOptions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    direction_ind: None | AirTripType = field(
        default=None,
        metadata={
            "name": "DirectionInd",
            "type": "Attribute",
        },
    )
    departure_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class OriginDestinationOptions:
        """
        Attributes:
            origin_destination_option: A container for flight segments.
        """

        origin_destination_option: list[OriginDestinationOptionType] = field(
            default_factory=list,
            metadata={
                "name": "OriginDestinationOption",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 99,
            },
        )
