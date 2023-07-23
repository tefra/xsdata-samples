from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_base_air_reservation import TypeBaseAirReservation

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirReservation(TypeBaseAirReservation):
    """
    The parent container for all booking data.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
