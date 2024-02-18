from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.credit_card_payment_auth import CreditCardPaymentAuth
from travelport.models.locator_code_1 import LocatorCode1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class CreditCardAuthReq(BaseReq1):
    """
    Performs a credit card authorization to validate a credit card for use during
    booking.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    locator_code: None | LocatorCode1 = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    credit_card_payment_auth: list[CreditCardPaymentAuth] = field(
        default_factory=list,
        metadata={
            "name": "CreditCardPaymentAuth",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    plating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        },
    )
