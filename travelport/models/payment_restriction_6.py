from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.address_restriction_6 import AddressRestriction6
from travelport.models.card_restriction_6 import CardRestriction6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class PaymentRestriction6:
    class Meta:
        name = "PaymentRestriction"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    card_restriction: list[CardRestriction6] = field(
        default_factory=list,
        metadata={
            "name": "CardRestriction",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    address_restriction: None | AddressRestriction6 = field(
        default=None,
        metadata={
            "name": "AddressRestriction",
            "type": "Element",
            "required": True,
        },
    )
