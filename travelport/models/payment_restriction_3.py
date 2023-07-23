from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.address_restriction_3 import AddressRestriction3
from travelport.models.card_restriction_3 import CardRestriction3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class PaymentRestriction3:
    class Meta:
        name = "PaymentRestriction"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    card_restriction: list[CardRestriction3] = field(
        default_factory=list,
        metadata={
            "name": "CardRestriction",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    address_restriction: None | AddressRestriction3 = field(
        default=None,
        metadata={
            "name": "AddressRestriction",
            "type": "Element",
            "required": True,
        }
    )
