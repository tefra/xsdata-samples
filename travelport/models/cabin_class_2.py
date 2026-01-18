from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class CabinClass2:
    """
    The cabin class (First, Business, Economy).
    """

    class Meta:
        name = "CabinClass"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
