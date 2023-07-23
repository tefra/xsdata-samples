from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_element import TypeElement

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class VehicleDelete:
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    element: None | TypeElement = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
