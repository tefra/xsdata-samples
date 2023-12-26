from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_voucher_information_1 import (
    TypeVoucherInformation1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class TypePaymentInformation:
    """
    Parameters
    ----------
    voucher
    billing_number
        A Billing Number that may be associated to the Voucher.
    billing_reference_number
        A Number Assigned for Billing reconciliation processes that may also
        include a Corporate Account ID
    pre_payment
        Amount paid in advance for  vehicle reservation. Can contain other
        non Money information to the vehicle supplier.
    """

    class Meta:
        name = "typePaymentInformation"

    voucher: None | TypeVoucherInformation1 = field(
        default=None,
        metadata={
            "name": "Voucher",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        },
    )
    billing_number: None | str = field(
        default=None,
        metadata={
            "name": "BillingNumber",
            "type": "Attribute",
        },
    )
    billing_reference_number: None | str = field(
        default=None,
        metadata={
            "name": "BillingReferenceNumber",
            "type": "Attribute",
        },
    )
    pre_payment: None | str = field(
        default=None,
        metadata={
            "name": "PrePayment",
            "type": "Attribute",
            "max_length": 90,
        },
    )
