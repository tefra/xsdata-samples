from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_restriction_1 import AddressRestriction1
from travelport.models.card_restriction_1 import CardRestriction1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class PaymentRestriction1:
    class Meta:
        name = "PaymentRestriction"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    card_restriction: list[CardRestriction1] = field(
        default_factory=list,
        metadata={
            "name": "CardRestriction",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    address_restriction: AddressRestriction1 = field(
        metadata={
            "name": "AddressRestriction",
            "type": "Element",
            "required": True,
        }
    )
