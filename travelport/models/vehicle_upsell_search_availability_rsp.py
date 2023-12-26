from __future__ import annotations
from dataclasses import dataclass
from travelport.models.base_vehicle_search_availability_rsp import (
    BaseVehicleSearchAvailabilityRsp,
)

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleUpsellSearchAvailabilityRsp(BaseVehicleSearchAvailabilityRsp):
    """
    Response of search Vehicle Upsell offer availability.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"
