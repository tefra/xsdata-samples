from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_date_options_1 import TypeDateOptions1
from travelport.models.type_payment_type_1 import TypePaymentType1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeSearchPaymentDetails1:
    """
    The Searchable fields on PaymentDetails.

    Parameters
    ----------
    expiration_date
    type_value
        Cash, Credit, etc.
    payment_supplier
        The supplier code of the payment. (VI, CA, AX, etc)
    account_number
        Payment account number (e.g. Credit Card Number, etc.)
    """

    class Meta:
        name = "typeSearchPaymentDetails"

    expiration_date: None | TypeDateOptions1 = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    type_value: None | TypePaymentType1 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    payment_supplier: None | str = field(
        default=None,
        metadata={
            "name": "PaymentSupplier",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    account_number: None | str = field(
        default=None,
        metadata={
            "name": "AccountNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
