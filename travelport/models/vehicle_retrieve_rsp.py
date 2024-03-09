from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.vehicle_reservation import VehicleReservation

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleRetrieveRsp(BaseRsp1):
    """
    Response to a VehicleRetrieveReq.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle_reservation: list[VehicleReservation] = field(
        default_factory=list,
        metadata={
            "name": "VehicleReservation",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
