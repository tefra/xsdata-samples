from __future__ import annotations
from dataclasses import dataclass
from travelport.models.base_vehicle_search_availability_req import (
    BaseVehicleSearchAvailabilityReq,
)

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleUpsellSearchAvailabilityReq(BaseVehicleSearchAvailabilityReq):
    """
    Request to search Upsell offer availability for Vehicle.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"
