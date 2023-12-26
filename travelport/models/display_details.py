from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.display_detail import DisplayDetail

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class DisplayDetails:
    """
    The container to display the contents of PNR in GDS format.

    Parameters
    ----------
    display_detail
    display_contents
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

    display_detail: list[DisplayDetail] = field(
        default_factory=list,
        metadata={
            "name": "DisplayDetail",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    display_contents: None | str = field(
        default=None,
        metadata={
            "name": "DisplayContents",
            "type": "Element",
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
