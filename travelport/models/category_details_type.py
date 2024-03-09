from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.value_details import ValueDetails

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class CategoryDetailsType:
    """
    Parameters
    ----------
    category_details
        For each category Details of Structured Fare Rules
    value
    """

    category_details: list[ValueDetails] = field(
        default_factory=list,
        metadata={
            "name": "CategoryDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )
