from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class FareRuleNameValue:
    """
    Fare Rule Name Value Pair, used in Short Rules.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    name: str = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    value: str = field(
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )
