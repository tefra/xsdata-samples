from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.form_of_payment_ref_1 import FormOfPaymentRef1
from travelport.models.waiver_code import WaiverCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirExchangeTicketBundle:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    ticket_number: None | str = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
            "min_length": 1,
            "max_length": 13,
        },
    )
    form_of_payment: list[FormOfPayment1] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 2,
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
    waiver_code: None | WaiverCode = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        },
    )
