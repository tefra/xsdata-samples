from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_location_2 import TypeLocation2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class ConnectionPoint2(TypeLocation2):
    """
    A connection point can be eith an IATA airport or cir city code.
    """

    class Meta:
        name = "ConnectionPoint"
        namespace = "http://www.travelport.com/schema/common_v32_0"
