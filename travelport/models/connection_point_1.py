from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_location_1 import TypeLocation1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class ConnectionPoint1(TypeLocation1):
    """
    A connection point can be eith an IATA airport or cir city code.
    """
    class Meta:
        name = "ConnectionPoint"
        namespace = "http://www.travelport.com/schema/common_v52_0"
