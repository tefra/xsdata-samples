from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class Endorsement6:
    """
    Restrictions or instructions about the fare or ticket.
    """
    class Meta:
        name = "Endorsement"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        }
    )
