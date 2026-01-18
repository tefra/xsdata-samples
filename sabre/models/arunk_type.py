from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.request_location_type import RequestLocationType
from sabre.models.side_trip_type import SideTripType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class ArunkType:
    """
    Attributes:
        origin_location: Origin code
        destination_location: Destination code
        side_trip: Side trip information
    """

    origin_location: RequestLocationType = field(
        metadata={
            "name": "OriginLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    destination_location: RequestLocationType = field(
        metadata={
            "name": "DestinationLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    side_trip: None | SideTripType = field(
        default=None,
        metadata={
            "name": "SideTrip",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
