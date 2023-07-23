from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_hotel_details_req import BaseHotelDetailsReq
from travelport.models.host_token_1 import HostToken1
from travelport.models.next_result_reference_1 import NextResultReference1

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelDetailsReq(BaseHotelDetailsReq):
    """
    Request to retrieve the details of a hotel property.

    Parameters
    ----------
    host_token
    next_result_reference
    return_media_links
        If true, return the media links. Not supported by all providers
    return_guest_reviews
        If true, return reviews and comments for the hotel property.  Not
        supported by all providers
    policy_reference
        This attribute will be used to pass in a value on the request which
        would be used to link to a ‘Policy Group’ in a policy engine
        external to UAPI.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    host_token: None | HostToken1 = field(
        default=None,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    next_result_reference: None | NextResultReference1 = field(
        default=None,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    return_media_links: bool = field(
        default=False,
        metadata={
            "name": "ReturnMediaLinks",
            "type": "Attribute",
        }
    )
    return_guest_reviews: bool = field(
        default=False,
        metadata={
            "name": "ReturnGuestReviews",
            "type": "Attribute",
        }
    )
    policy_reference: None | str = field(
        default=None,
        metadata={
            "name": "PolicyReference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        }
    )
