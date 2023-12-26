from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.required_field_6 import RequiredField6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class AddressRestriction6:
    class Meta:
        name = "AddressRestriction"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    required_field: list[RequiredField6] = field(
        default_factory=list,
        metadata={
            "name": "RequiredField",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
