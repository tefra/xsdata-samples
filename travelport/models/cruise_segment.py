from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.cruise_stay import CruiseStay
from travelport.models.segment_1 import Segment1

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass
class CruiseSegment(Segment1):
    """
    An Cruise marketable travel segment.

    Parameters
    ----------
    cruise_stay
    vendor
        Cruise Vendor Code.
    vendor_name
        Cruise Vendor Name.
    origin
        The location code for the origin of cruise segment.
    destination
        The location code for the destination of cruise segment.
    departure_time
        The date and time at which this cruise segment departs from the
        origin.
    arrival_time
        The date and time at which this cruise segment arrives at the
        destination.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    cruise_stay: None | CruiseStay = field(
        default=None,
        metadata={
            "name": "CruiseStay",
            "type": "Element",
            "required": True,
        },
    )
    vendor: None | str = field(
        default=None,
        metadata={
            "name": "Vendor",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 3,
        },
    )
    vendor_name: None | str = field(
        default=None,
        metadata={
            "name": "VendorName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        },
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
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
