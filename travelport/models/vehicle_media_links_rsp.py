from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.vehicle_with_media_items import VehicleWithMediaItems

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class VehicleMediaLinksRsp(BaseRsp1):
    """
    Response for vehicle image search results.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle_with_media_items: list[VehicleWithMediaItems] = field(
        default_factory=list,
        metadata={
            "name": "VehicleWithMediaItems",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
