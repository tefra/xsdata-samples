from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_vehicle_types import TypeVehicleTypes

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class VehicleType:
    """
    A standard list or classification of vehicle types .
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    value: TypeVehicleTypes = field(
        metadata={
            "required": True,
        }
    )
