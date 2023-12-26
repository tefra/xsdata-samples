from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_create_reservation_req_6 import (
    BaseCreateReservationReq6,
)
from travelport.models.form_of_payment_8 import FormOfPayment8

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class BaseCreateWithFormOfPaymentReq6(BaseCreateReservationReq6):
    """
    Container for BaseCreateReservation along with Form Of Payment.

    Parameters
    ----------
    form_of_payment
        Provider:1G,1V,1P,1J,ACH,SDK.
    """

    class Meta:
        name = "BaseCreateWithFormOfPaymentReq"

    form_of_payment: list[FormOfPayment8] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        },
    )
