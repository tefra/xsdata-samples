from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.charge import Charge
from travelport.models.equipment import Equipment

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class PricedEquip:
    """
    Special Equipment detail and charge for rental.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    equipment: None | Equipment = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Element",
        },
    )
    charge: None | Charge = field(
        default=None,
        metadata={
            "name": "Charge",
            "type": "Element",
        },
    )
