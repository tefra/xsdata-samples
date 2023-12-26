from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BookingCodeInfo:
    """Details Cabin class info and class of service information with availability
    counts.

    Only provided on search results and grouped by Cabin class

    Parameters
    ----------
    cabin_class
        Specifies Cabin class for a group of class of services. Cabin class
        is not identified if it is not present.
    booking_counts
        Lists class of service and their counts for specific cabin class
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    cabin_class: None | str = field(
        default=None,
        metadata={
            "name": "CabinClass",
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
