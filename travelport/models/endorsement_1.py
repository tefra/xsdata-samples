from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class Endorsement1:
    """
    Restrictions or instructions about the fare or ticket.
    """

    class Meta:
        name = "Endorsement"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    value: str = field(
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        }
    )
