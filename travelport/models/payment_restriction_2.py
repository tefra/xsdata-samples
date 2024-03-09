from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_restriction_2 import AddressRestriction2
from travelport.models.card_restriction_2 import CardRestriction2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class PaymentRestriction2:
    class Meta:
        name = "PaymentRestriction"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    card_restriction: list[CardRestriction2] = field(
        default_factory=list,
        metadata={
            "name": "CardRestriction",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    address_restriction: None | AddressRestriction2 = field(
        default=None,
        metadata={
            "name": "AddressRestriction",
            "type": "Element",
            "required": True,
        },
    )
