from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.required_field_2 import RequiredField2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class AddressRestriction2:
    class Meta:
        name = "AddressRestriction"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    required_field: list[RequiredField2] = field(
        default_factory=list,
        metadata={
            "name": "RequiredField",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
