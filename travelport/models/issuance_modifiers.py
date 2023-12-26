from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.customer_receipt_info import CustomerReceiptInfo
from travelport.models.emdcommission import Emdcommission
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.form_of_payment_ref_1 import FormOfPaymentRef1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class IssuanceModifiers:
    """
    General modifiers supported for EMD Issuance.Supported providers are 1V/1G/1P.

    Parameters
    ----------
    form_of_payment_ref
        Reference to FormOfPayment present in the UR to be used for EMD
        issuance.
    form_of_payment
        FormOfPayment information to be used for EMD issuance.
    customer_receipt_info
        Information about customer receipt via email.
    emdendorsement
        Endorsement details to be used during EMD issuance.
    emdcommission
        Commission information to be used for EMD issuance.
    plating_carrier
        Plating carrier code for which this EMD is issued.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    form_of_payment_ref: None | FormOfPaymentRef1 = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    customer_receipt_info: None | CustomerReceiptInfo = field(
        default=None,
        metadata={
            "name": "CustomerReceiptInfo",
            "type": "Element",
        },
    )
    emdendorsement: None | str = field(
        default=None,
        metadata={
            "name": "EMDEndorsement",
            "type": "Element",
            "min_length": 1,
            "max_length": 255,
        },
    )
    emdcommission: None | Emdcommission = field(
        default=None,
        metadata={
            "name": "EMDCommission",
            "type": "Element",
        },
    )
    plating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
