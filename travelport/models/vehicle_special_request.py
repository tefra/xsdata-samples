from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleSpecialRequest:
    """
    Make a textual request to the Vehicle supplier.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 250,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
