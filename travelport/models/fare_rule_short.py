from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.fare_rule_name_value import FareRuleNameValue

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareRuleShort:
    """
    Short Text Fare Rule.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_rule_name_value: list[FareRuleNameValue] = field(
        default_factory=list,
        metadata={
            "name": "FareRuleNameValue",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    category: None | int = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
    table_number: None | str = field(
        default=None,
        metadata={
            "name": "TableNumber",
            "type": "Attribute",
        }
    )
