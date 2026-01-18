from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class TypeApplicableSegment:
    """
    Parameters
    ----------
    key
    air_itinerary_details_ref
    booking_counts
        Classes of service and their counts.
    """

    class Meta:
        name = "typeApplicableSegment"

    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    air_itinerary_details_ref: None | str = field(
        default=None,
        metadata={
            "name": "AirItineraryDetailsRef",
            "type": "Attribute",
        },
    )
    booking_counts: None | str = field(
        default=None,
        metadata={
            "name": "BookingCounts",
            "type": "Attribute",
        },
    )
