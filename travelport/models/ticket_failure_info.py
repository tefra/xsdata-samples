from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_pricing_info_ref import AirPricingInfoRef
from travelport.models.name_1 import Name1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TicketFailureInfo:
    """Will be optionally returned as part of AirTicketingRsp if one or all ticket
    requests fail.

    Atrributes are faiilure code, failure message, and passenger
    reference key. Passenger name is a child element.

    Parameters
    ----------
    air_pricing_info_ref
        Returns related air pricing infos.
    name
    code
    message
    booking_traveler_ref
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_pricing_info_ref: list[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    name: None | Name1 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        },
    )
    code: None | int = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        },
    )
    message: None | str = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Attribute",
        },
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        },
    )
