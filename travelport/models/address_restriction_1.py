from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.required_field_1 import RequiredField1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class AddressRestriction1:
    class Meta:
        name = "AddressRestriction"
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
