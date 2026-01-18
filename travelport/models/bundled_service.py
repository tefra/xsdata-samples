from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_booking import TypeBooking

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class BundledService:
    """
    Displays the services bundled together.

    Parameters
    ----------
    carrier
        Carrier the service is applicable.
    carrier_sub_code
        Carrier sub code. True means the carrier used their own sub code.
        False means the carrier used an ATPCO sub code
    service_type
        The type of service or what the service is used for, e.g. F type is
        flight type, meaning the service is used on a flight
    service_sub_code
        The sub code of the service, e.g. OAA for Pre paid baggage
    name
        Name of the bundled service.
    booking
        Booking method for the bundled service, e..g SSR.
    occurrence
        How many of the service are included in the bundled service.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    carrier_sub_code: None | bool = field(
        default=None,
        metadata={
            "name": "CarrierSubCode",
            "type": "Attribute",
        },
    )
    service_type: None | str = field(
        default=None,
        metadata={
            "name": "ServiceType",
            "type": "Attribute",
        },
    )
    service_sub_code: None | str = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    booking: None | TypeBooking = field(
        default=None,
        metadata={
            "name": "Booking",
            "type": "Attribute",
        },
    )
    occurrence: None | int = field(
        default=None,
        metadata={
            "name": "Occurrence",
            "type": "Attribute",
        },
    )
