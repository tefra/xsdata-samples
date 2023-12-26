from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_refund_bundle import AirRefundBundle
from travelport.models.air_refund_modifiers import AirRefundModifiers
from travelport.models.base_req_1 import BaseReq1
from travelport.models.commission_1 import Commission1
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.tcrrefund_bundle import TcrrefundBundle

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirRefundReq(BaseReq1):
    """
    Request to refund an itinerary for the amount previously quoted.

    Parameters
    ----------
    air_refund_bundle
        Provider: ACH.
    tcrrefund_bundle
        Provider: ACH.
    air_refund_modifiers
    commission
        Provider: ACH.
    form_of_payment
        Provider: ACH-Form of Payment for any Additional Collection charges
        for the Refund.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_refund_bundle: list[AirRefundBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirRefundBundle",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    tcrrefund_bundle: list[TcrrefundBundle] = field(
        default_factory=list,
        metadata={
            "name": "TCRRefundBundle",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_refund_modifiers: None | AirRefundModifiers = field(
        default=None,
        metadata={
            "name": "AirRefundModifiers",
            "type": "Element",
        },
    )
    commission: list[Commission1] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 9,
        },
    )
    form_of_payment: None | FormOfPayment1 = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
