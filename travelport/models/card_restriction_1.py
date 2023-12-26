from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.required_field_1 import RequiredField1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class CardRestriction1:
    """
    Parameters
    ----------
    required_field
    code
        2 letter Credit/Debit Card merchant type
    name
        Card merchant description
    """

    class Meta:
        name = "CardRestriction"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    required_field: list[RequiredField1] = field(
        default_factory=list,
        metadata={
            "name": "RequiredField",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 2,
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        },
    )
