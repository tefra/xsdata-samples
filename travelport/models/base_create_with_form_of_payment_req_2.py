from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_create_reservation_req_2 import (
    BaseCreateReservationReq2,
)
from travelport.models.form_of_payment_3 import FormOfPayment3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class BaseCreateWithFormOfPaymentReq2(BaseCreateReservationReq2):
    """
    Container for BaseCreateReservation along with Form Of Payment.

    Parameters
    ----------
    form_of_payment
        Provider:1G,1V,1P,1J,ACH,SDK.
    """

    class Meta:
        name = "BaseCreateWithFormOfPaymentReq"

    form_of_payment: list[FormOfPayment3] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
            "max_occurs": 999,
        },
    )
