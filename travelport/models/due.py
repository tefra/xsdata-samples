from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass(kw_only=True)
class Due:
    """
    Due balance Amount on Booking.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"
