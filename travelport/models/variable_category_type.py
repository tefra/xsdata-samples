from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.category_details_type import CategoryDetailsType
from travelport.models.value_details import ValueDetails

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class VariableCategoryType:
    """
    Parameters
    ----------
    category_details
        To indicate details of which category is displayed
    variable_category_detail
        If the specified category of Structured Fare Rules is of variable
        lenght
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
    variable_category_detail: list[CategoryDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "VariableCategoryDetail",
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
