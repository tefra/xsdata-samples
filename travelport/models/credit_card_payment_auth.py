from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.credit_card_1 import CreditCard1
from travelport.models.form_of_payment_ref_1 import FormOfPaymentRef1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class CreditCardPaymentAuth:
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    credit_card: None | CreditCard1 = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    form_of_payment_ref: None | FormOfPaymentRef1 = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    security_code: None | str = field(
        default=None,
        metadata={
            "name": "SecurityCode",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        },
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        },
    )
    perform_avs: None | bool = field(
        default=None,
        metadata={
            "name": "PerformAVS",
            "type": "Attribute",
            "required": True,
        },
    )
