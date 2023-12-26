from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_create_reservation_req_1 import (
    BaseCreateReservationReq1,
)
from travelport.models.form_of_payment_1 import FormOfPayment1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class BaseCreateWithFormOfPaymentReq1(BaseCreateReservationReq1):
    """
    Container for BaseCreateReservation along with Form Of Payment.

    Parameters
    ----------
    form_of_payment
        Provider:1G,1V,1P,ACH,SDK.
    """

    class Meta:
        name = "BaseCreateWithFormOfPaymentReq"

    form_of_payment: list[FormOfPayment1] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
