from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass(kw_only=True)
class Command:
    """
    The command to pass to the host.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
