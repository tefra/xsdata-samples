from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_search_rsp_1 import BaseSearchRsp1
from travelport.models.vehicle import Vehicle
from travelport.models.vehicle_date_location import VehicleDateLocation

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class BaseVehicleSearchAvailabilityRsp(BaseSearchRsp1):
    """
    Base response of vehicle availability response.
    """

    vehicle_date_location: VehicleDateLocation = field(
        metadata={
            "name": "VehicleDateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "required": True,
        }
    )
    vehicle: list[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        },
    )
