from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.required_field_4 import RequiredField4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class AddressRestriction4:
    class Meta:
        name = "AddressRestriction"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    required_field: list[RequiredField4] = field(
        default_factory=list,
        metadata={
            "name": "RequiredField",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
