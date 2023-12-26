from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_location_3 import TypeLocation3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class ConnectionPoint3(TypeLocation3):
    """
    A connection point can be eith an IATA airport or cir city code.
    """

    class Meta:
        name = "ConnectionPoint"
        namespace = "http://www.travelport.com/schema/common_v33_0"
