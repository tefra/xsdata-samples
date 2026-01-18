from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_date_options_2 import TypeDateOptions2
from travelport.models.type_payment_type_2 import TypePaymentType2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TypeSearchPaymentDetails2:
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

    expiration_date: None | TypeDateOptions2 = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    type_value: TypePaymentType2 = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
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
