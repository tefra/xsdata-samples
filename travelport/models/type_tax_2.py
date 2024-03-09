from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class TypeTax2:
    class Meta:
        name = "typeTax"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        },
    )
