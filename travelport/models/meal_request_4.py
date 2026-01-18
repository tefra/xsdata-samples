from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class MealRequest4:
    """
    Special meal requests like Vegetarian.
    """

    class Meta:
        name = "MealRequest"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "length": 4,
        }
    )
