from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from travelport.models.booking_info import BookingInfo
from travelport.models.connection import Connection

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Option:
    """
    List of segment and fare available for the search air leg.

    Parameters
    ----------
    booking_info
    connection
    key
    travel_time
        Total traveling time that is difference between the departure time
        of the first segment and the arrival time of the last segments for
        that particular entire set of connection.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    booking_info: list[BookingInfo] = field(
        default_factory=list,
        metadata={
            "name": "BookingInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    connection: list[Connection] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
    travel_time: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
        },
    )
