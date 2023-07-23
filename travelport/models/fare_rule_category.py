from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareRuleCategory:
    """
    Rule Categories to filter on.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    category: None | int = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 50,
        }
    )
