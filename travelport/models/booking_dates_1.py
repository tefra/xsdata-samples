from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class BookingDates1:
    """
    Check in and Check out Date information.
    """

    class Meta:
        name = "BookingDates"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    check_in_date: None | str = field(
        default=None,
        metadata={
            "name": "CheckInDate",
            "type": "Attribute",
            "pattern": r"[^:Z].*",
        },
    )
    check_out_date: None | str = field(
        default=None,
        metadata={
            "name": "CheckOutDate",
            "type": "Attribute",
            "pattern": r"[^:Z].*",
        },
    )
