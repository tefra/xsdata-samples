from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.fare_rule_category_types import FareRuleCategoryTypes

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class StructuredFareRulesType:
    """
    Parameters
    ----------
    fare_rule_category_type
        For FareRulesType element
    """

    fare_rule_category_type: list[FareRuleCategoryTypes] = field(
        default_factory=list,
        metadata={
            "name": "FareRuleCategoryType",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        },
    )
