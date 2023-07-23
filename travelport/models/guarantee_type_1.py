from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class GuaranteeType1:
    """
    A type of guarantee i.e.
    """
    class Meta:
        name = "GuaranteeType"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 250,
        }
    )
