from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.phone_number_1 import PhoneNumber1
from travelport.models.type_structured_address_1 import TypeStructuredAddress1

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class DeliveryAddress(TypeStructuredAddress1):
    """
    An address to which a rental car should be delivered and a phone number
    associated with the address.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    phone_number: None | PhoneNumber1 = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
