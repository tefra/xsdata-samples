from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.vehicle_location import VehicleLocation

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleLocationRsp(BaseRsp1):
    """
    Returns a list of vendors and their locations for an airport or city code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle_location: list[VehicleLocation] = field(
        default_factory=list,
        metadata={
            "name": "VehicleLocation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
