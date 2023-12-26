from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BookingCode:
    """
    The Booking Code (Class of Service) for a segment.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 2,
        },
    )
