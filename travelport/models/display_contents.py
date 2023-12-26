from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class DisplayContents:
    """
    Display the contents in GDS format.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
