from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_rail_create_reservation_rsp import (
    TypeRailCreateReservationRsp,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class RailCreateReservationRsp(TypeRailCreateReservationRsp):
    """
    Returns rail reservation information with ticketing info etc..
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"
