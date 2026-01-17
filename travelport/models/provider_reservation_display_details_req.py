from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class ProviderReservationDisplayDetailsReq(BaseReq1):
    """
    Request to display the addtional details of provider reservation
    information .

    Parameters
    ----------
    provider_code
    provider_locator_code
    provider_reservation_detail
        Provider Reservation data exists.
    custom_check
        Custom check data exists.
    provider_profile
        Provider Profile data exists.
    divide_details
        Divide Details data exists.
    enhanced_itin_modifiers
        Enhanced itinerary modifiers data exists
    integrated_content
        Integrated content data exists
    cruise
        Cruise data exists.
    rail_segment
        Rail Segment data exists.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        },
    )
    provider_reservation_detail: None | bool = field(
        default=None,
        metadata={
            "name": "ProviderReservationDetail",
            "type": "Attribute",
        },
    )
    custom_check: None | bool = field(
        default=None,
        metadata={
            "name": "CustomCheck",
            "type": "Attribute",
        },
    )
    provider_profile: None | bool = field(
        default=None,
        metadata={
            "name": "ProviderProfile",
            "type": "Attribute",
        },
    )
    divide_details: None | bool = field(
        default=None,
        metadata={
            "name": "DivideDetails",
            "type": "Attribute",
        },
    )
    enhanced_itin_modifiers: None | bool = field(
        default=None,
        metadata={
            "name": "EnhancedItinModifiers",
            "type": "Attribute",
        },
    )
    integrated_content: None | bool = field(
        default=None,
        metadata={
            "name": "IntegratedContent",
            "type": "Attribute",
        },
    )
    cruise: None | bool = field(
        default=None,
        metadata={
            "name": "Cruise",
            "type": "Attribute",
        },
    )
    rail_segment: None | bool = field(
        default=None,
        metadata={
            "name": "RailSegment",
            "type": "Attribute",
        },
    )
