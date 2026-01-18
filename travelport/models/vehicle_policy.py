from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.vehicle_detail import VehicleDetail
from travelport.models.vehicle_disclaimer import VehicleDisclaimer

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class VehiclePolicy:
    """
    Policy information provided by the Vehicle Supplier.

    Usually relative to a specific location.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle_disclaimer: list[VehicleDisclaimer] = field(
        default_factory=list,
        metadata={
            "name": "VehicleDisclaimer",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    vehicle_detail: list[VehicleDetail] = field(
        default_factory=list,
        metadata={
            "name": "VehicleDetail",
            "type": "Element",
            "max_occurs": 999,
        },
    )
