from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.connection_type import ConnectionType
from sabre.models.request_location_type import RequestLocationType
from sabre.models.travel_date_time_type import TravelDateTimeType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class OriginDestinationInformationType(TravelDateTimeType):
    """
    Origin and Destination location, and time information for the request.

    Also includes the ability to specify a connection location for the
    search.

    Attributes:
        origin_location: Travel Origin Location - for example, air uses
            the IATA 3 letter code.
        destination_location: Travel Destination Location - for example,
            air uses the IATA 3 letter code.
        connection_locations: Travel Connection Location - for example,
            air uses the IATA 3 letter code.
    """

    origin_location: None | OriginDestinationInformationType.OriginLocation = (
        field(
            default=None,
            metadata={
                "name": "OriginLocation",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "required": True,
            },
        )
    )
    destination_location: (
        None | OriginDestinationInformationType.DestinationLocation
    ) = field(
        default=None,
        metadata={
            "name": "DestinationLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    connection_locations: None | ConnectionType = field(
        default=None,
        metadata={
            "name": "ConnectionLocations",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )

    @dataclass
    class OriginLocation(RequestLocationType):
        """
        Attributes:
            all_airports: Flag indicating if all cached origin cities
                are to be processed as origin airports.
        """

        all_airports: None | bool = field(
            default=None,
            metadata={
                "name": "AllAirports",
                "type": "Attribute",
            },
        )

    @dataclass
    class DestinationLocation(RequestLocationType):
        """
        Attributes:
            all_airports: Flag indicating if all cached destination
                cities are to be processed as destination airports.
        """

        all_airports: None | bool = field(
            default=None,
            metadata={
                "name": "AllAirports",
                "type": "Attribute",
            },
        )
