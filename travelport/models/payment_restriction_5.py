from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_restriction_5 import AddressRestriction5
from travelport.models.card_restriction_5 import CardRestriction5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class PaymentRestriction5:
    class Meta:
        name = "PaymentRestriction"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    card_restriction: list[CardRestriction5] = field(
        default_factory=list,
        metadata={
            "name": "CardRestriction",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    address_restriction: AddressRestriction5 = field(
        metadata={
            "name": "AddressRestriction",
            "type": "Element",
            "required": True,
        }
    )
