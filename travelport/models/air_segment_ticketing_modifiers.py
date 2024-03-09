from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirSegmentTicketingModifiers:
    """Specifies modifiers that a particular segment should be priced with.

    If this is used, then there must be one for each AirSegment in the
    AirItinerary.

    Parameters
    ----------
    air_segment_ref
    brand_tier
        Modifier to price by specific brand tier number.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Attribute",
        },
    )
    brand_tier: None | str = field(
        default=None,
        metadata={
            "name": "BrandTier",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        },
    )
