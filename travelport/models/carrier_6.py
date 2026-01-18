from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class Carrier6:
    """
    Carrier identifier.
    """

    class Meta:
        name = "Carrier"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    code: str = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
