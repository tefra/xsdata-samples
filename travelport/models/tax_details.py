from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.tax_2 import Tax2

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class TaxDetails:
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    tax: list[Tax2] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
