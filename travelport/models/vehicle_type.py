from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_vehicle_types import TypeVehicleTypes

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleType:
    """
    A standard list or classification of vehicle types .
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    value: None | TypeVehicleTypes = field(
        default=None,
        metadata={
            "required": True,
        },
    )
