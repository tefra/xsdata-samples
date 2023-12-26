from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_fare_rule_category_code import (
    TypeFareRuleCategoryCode,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirFareRuleCategory:
    """
    A collection of fare rule category codes.

    Parameters
    ----------
    category_code
        The Category Code for Air Fare Rule.
    fare_info_ref
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    category_code: list[TypeFareRuleCategoryCode] = field(
        default_factory=list,
        metadata={
            "name": "CategoryCode",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
    fare_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
        },
    )
