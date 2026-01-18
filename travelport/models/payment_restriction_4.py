from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_restriction_4 import AddressRestriction4
from travelport.models.card_restriction_4 import CardRestriction4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class PaymentRestriction4:
    class Meta:
        name = "PaymentRestriction"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    card_restriction: list[CardRestriction4] = field(
        default_factory=list,
        metadata={
            "name": "CardRestriction",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    address_restriction: AddressRestriction4 = field(
        metadata={
            "name": "AddressRestriction",
            "type": "Element",
            "required": True,
        }
    )
