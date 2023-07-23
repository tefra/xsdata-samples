from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_location_4 import TypeLocation4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class ConnectionPoint4(TypeLocation4):
    """
    A connection point can be eith an IATA airport or cir city code.
    """
    class Meta:
        name = "ConnectionPoint"
        namespace = "http://www.travelport.com/schema/common_v37_0"
