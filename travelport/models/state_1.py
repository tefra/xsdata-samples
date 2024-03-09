from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class State1:
    """
    Container to house the state code for an address.
    """

    class Meta:
        name = "State"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
