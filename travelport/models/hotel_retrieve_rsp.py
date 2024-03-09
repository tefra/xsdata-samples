from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.hotel_reservation import HotelReservation

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelRetrieveRsp(BaseRsp1):
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_reservation: list[HotelReservation] = field(
        default_factory=list,
        metadata={
            "name": "HotelReservation",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
