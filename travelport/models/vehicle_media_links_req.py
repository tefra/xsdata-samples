from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.vehicle_pickup_location import VehiclePickupLocation
from travelport.models.vehicle_search_id import VehicleSearchId

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleMediaLinksReq(BaseReq1):
    """
    Used to request a list of images for a location (airport or city code) and
    vendor.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle_search_id: None | VehicleSearchId = field(
        default=None,
        metadata={
            "name": "VehicleSearchId",
            "type": "Element",
        },
    )
    vehicle_pickup_location: list[VehiclePickupLocation] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePickupLocation",
            "type": "Element",
            "max_occurs": 999,
        },
    )
