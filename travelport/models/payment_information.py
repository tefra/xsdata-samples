from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_payment_information import TypePaymentInformation

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class PaymentInformation(TypePaymentInformation):
    """
    The payment information for a vehicle reservation.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
