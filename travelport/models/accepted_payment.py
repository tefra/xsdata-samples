from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class AcceptedPayment:
    """
    Parameters
    ----------
    payment_code
        The issuer of the form of payment, such as the credit card bank.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    payment_code: None | str = field(
        default=None,
        metadata={
            "name": "PaymentCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 2,
        }
    )
