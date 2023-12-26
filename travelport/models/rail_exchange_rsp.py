from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_rail_reservation_rsp import TypeRailReservationRsp

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailExchangeRsp(TypeRailReservationRsp):
    """
    Returns rail exchange reservation information with ticketing/refund info etc..
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"
