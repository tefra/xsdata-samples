from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_fare_rule_category import AirFareRuleCategory

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirFareRulesModifier:
    """
    The modifiers for Air Fare Rules.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_fare_rule_category: list[AirFareRuleCategory] = field(
        default_factory=list,
        metadata={
            "name": "AirFareRuleCategory",
            "type": "Element",
            "max_occurs": 999,
        },
    )
