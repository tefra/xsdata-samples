from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.required_field_6 import RequiredField6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class CardRestriction6:
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
        namespace = "http://www.travelport.com/schema/common_v38_0"

    required_field: list[RequiredField6] = field(
        default_factory=list,
        metadata={
            "name": "RequiredField",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 2,
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
