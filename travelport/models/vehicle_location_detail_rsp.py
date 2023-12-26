from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.location_info import LocationInfo
from travelport.models.vehicle_policy import VehiclePolicy
from travelport.models.vendor_info import VendorInfo

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleLocationDetailRsp(BaseRsp1):
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vendor_info: None | VendorInfo = field(
        default=None,
        metadata={
            "name": "VendorInfo",
            "type": "Element",
            "required": True,
        },
    )
    location_info: list[LocationInfo] = field(
        default_factory=list,
        metadata={
            "name": "LocationInfo",
            "type": "Element",
            "max_occurs": 2,
        },
    )
    vehicle_policy: None | VehiclePolicy = field(
        default=None,
        metadata={
            "name": "VehiclePolicy",
            "type": "Element",
        },
    )
