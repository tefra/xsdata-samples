from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_create_reservation_req_5 import BaseCreateReservationReq5
from travelport.models.form_of_payment_7 import FormOfPayment7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class BaseCreateWithFormOfPaymentReq5(BaseCreateReservationReq5):
    """
    Container for BaseCreateReservation along with Form Of Payment.

    Parameters
    ----------
    form_of_payment
        Provider:1G,1V,1P,1J,ACH,SDK.
    """
    class Meta:
        name = "BaseCreateWithFormOfPaymentReq"

    form_of_payment: list[FormOfPayment7] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
            "max_occurs": 999,
        }
    )
