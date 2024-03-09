from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.guest_reviews import GuestReviews
from travelport.models.host_token_1 import HostToken1
from travelport.models.hotel_alternate_properties import (
    HotelAlternateProperties,
)
from travelport.models.next_result_reference_1 import NextResultReference1
from travelport.models.requested_hotel_details import RequestedHotelDetails

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelDetailsRsp(BaseRsp1):
    """
    Response showing details of a given hotel property.

    Parameters
    ----------
    next_result_reference
    host_token
    requested_hotel_details
        Supported Provider GDS – 1G, 1V, 1P.
    hotel_alternate_properties
    guest_reviews
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    next_result_reference: None | NextResultReference1 = field(
        default=None,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    host_token: None | HostToken1 = field(
        default=None,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    requested_hotel_details: None | RequestedHotelDetails = field(
        default=None,
        metadata={
            "name": "RequestedHotelDetails",
            "type": "Element",
        },
    )
    hotel_alternate_properties: None | HotelAlternateProperties = field(
        default=None,
        metadata={
            "name": "HotelAlternateProperties",
            "type": "Element",
        },
    )
    guest_reviews: None | GuestReviews = field(
        default=None,
        metadata={
            "name": "GuestReviews",
            "type": "Element",
        },
    )
